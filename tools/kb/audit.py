#!/usr/bin/env python3
"""Offline KB audit. Raw CSV/evidence are inputs, generated catalogs are disposable."""
import argparse, collections, csv, hashlib, json, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[2]
ID = re.compile(r'\b(?:CMD|QRY|EVT|PROTO|RULE|TEST|CAP|REV|OBS|DISC)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b')
STATUSES = {'CONFIRMED','DOCUMENTED','APK-VERIFIED','EXPERIMENTAL','REJECTED','SUPERSEDED'}
EXCLUDED = {'registry/audit/catalog.json','registry/audit/findings.json','registry/audit/occurrences.md','registry/audit/inventory.json'}

def dump(obj): return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
def status(raw):
    # Conservative legacy classification. Original qualifiers and scope ALWAYS retained.
    if raw == 'REJECTED': return 'REJECTED'
    if raw in {'CONFIRMED','CONFIRMED-A97','CONFIRMED-WRITE-ONLY','CONFIRMED-IN-AIRCONTROL','HARDWARE-VERIFIED','APK-VERIFIED + HARDWARE-VERIFIED'}: return 'CONFIRMED'
    if 'DOCUMENTED' in raw: return 'DOCUMENTED'
    if 'APK-VERIFIED' in raw or 'SOURCE-CONFIRMED' in raw or 'CALL-SITE' in raw: return 'APK-VERIFIED'
    return 'EXPERIMENTAL'  # CAPTURED/IMPLEMENTED alone do not prove successful execution.

def audit(root=ROOT):
    issues=[]; rows=[]; occurrences=collections.defaultdict(list); inventory=[]
    def issue(kind,**kw): issues.append({'kind':kind,**kw})
    texts={}
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc':continue
        rel=p.relative_to(root).as_posix()
        if rel in EXCLUDED:continue
        data=p.read_bytes(); inventory.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        try: s=data.decode('utf-8')
        except UnicodeDecodeError:continue
        texts[rel]=s
        if p.suffix in {'.md','.csv','.json','.yaml','.yml'}:
            for n,line in enumerate(s.splitlines(),1):
                for ident in set(ID.findall(line)): occurrences[ident].append({'path':rel,'line':n})
    for p in sorted((root/'registry/records').glob('*.csv')):
        with p.open(newline='',encoding='utf-8') as f:
            for n,r in enumerate(csv.DictReader(f),2):
                loc={'path':p.relative_to(root).as_posix(),'row':n}
                if None in r or any(v is None for v in r.values()):issue('malformed_csv',**loc)
                if not r.get('ID') or not ID.fullmatch(r['ID']):issue('invalid_id',**loc)
                for k in ['Family','Device','Function','Protocol','Command / mechanism','Status']:
                    if not r.get(k):issue('missing_field',field=k,**loc)
                rows.append((loc,r))
    grouped=collections.defaultdict(list)
    for loc,r in rows:grouped[r['ID']].append((loc,r))
    decisions=json.loads((root/'registry/KB_DECISIONS.json').read_text())
    for loc,r in rows:
        if r.get('Status') not in decisions.get('legacy_status_vocabulary', {r.get('Status')}):
            issue('unknown_legacy_status',id=r.get('ID'),status=r.get('Status'),**loc)
    for ident,group in grouped.items():
        if len(group)>1:
            allowed=decisions['duplicate_ids'].get(ident)
            current=[{'path':loc['path'],'sha256':hashlib.sha256(dump(r).encode()).hexdigest()} for loc,r in group]
            if not allowed or allowed['occurrences'] != current:issue('duplicate_id',id=ident,occurrences=current)
    # Only exact context+mechanism is a duplicate candidate; never merge across device/protocol.
    signatures=collections.defaultdict(list)
    for loc,r in rows:
        sig=tuple(r[k].strip() for k in ['Device','Protocol','Command / mechanism'])
        signatures[sig].append(r['ID'])
    for sig,identifiers in signatures.items():
        if len(set(identifiers))>1:issue('same_context_mechanism',ids=sorted(set(identifiers)),context=sig)
    # Markdown inline and reference links; ignore fenced examples, external URLs and templates.
    for rel,s in texts.items():
        if not rel.endswith('.md'):continue
        in_fence=False
        for n,line in enumerate(s.splitlines(),1):
            if re.match(r'^\s*(```|~~~)',line):in_fence=not in_fence;continue
            if in_fence:continue
            links=re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s]+?)(?:\s+"[^"]*")?\)',line)
            m=re.match(r'^\s*\[[^\]]+\]:\s*(\S+)',line)
            if m:links.append(m[1])
            for dest in links:
                dest=dest.strip('<>'); u=urlsplit(dest)
                if u.scheme or u.netloc:continue
                if any(x in dest for x in ['<','>','*','{','}']):continue
                target=(root/u.path.lstrip('/') if u.path.startswith('/') else root/Path(rel).parent/unquote(u.path)).resolve() if u.path else root/rel
                if not target.exists():issue('broken_link',path=rel,line=n,target=dest);continue
                if u.fragment and target.is_file() and target.suffix=='.md':
                    anchors=[]; seen=collections.Counter()
                    for heading in target.read_text().splitlines():
                        if not heading.startswith('#'):continue
                        h=re.sub(r'^#+\s*','',heading).strip().lower()
                        h=re.sub(r'[^\w\- ]','',h).replace(' ','-'); num=seen[h];seen[h]+=1
                        anchors.append(h+(f'-{num}' if num else ''))
                    anchors+=re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)',target.read_text())
                    if unquote(u.fragment) not in anchors:issue('broken_anchor',path=rel,line=n,target=dest)
    catalog=[]
    for ident,group in sorted(grouped.items()):
        loc,r=group[0]; mentions=occurrences.get(ident,[])
        views=sorted({o['path'] for o in mentions if o['path'].startswith(('devices/','protocols/','functions/'))})
        if not views:issue('no_technical_view',id=ident)
        # Explicit per-row sources vs evidence discovery links are deliberately distinct.
        explicit=r.get('Source','')
        if not explicit:issue('missing_explicit_row_source',id=ident,path=loc['path'])
        catalog.append({'id':ident,'legacy_status':r['Status'],'classification':status(r['Status']),
            'device_scope':r['Device'],'classification_scope':('A97 only, not the full legacy Device column' if r['Status']=='CONFIRMED-A97' else 'exact legacy context; not all listed products/firmware'),'firmware':'not specified in CSV; consult linked evidence',
            'protocol':r['Protocol'],'mechanism':r['Command / mechanism'],'notes':r['Response / notes'],
            'explicit_source':explicit or None,'raw_occurrences':[l for l,_ in group],
            'technical_views':views,'mentions':mentions,
            'contextual_evidence':decisions['contextual_evidence'].get(ident,[])})
    for ident,claims in decisions['contextual_evidence'].items():
        if ident not in grouped:
            catalog.append({'id':ident,'origin':'technical-document / contextual evidence; no historical CSV row',
                'mentions':occurrences.get(ident,[]),'contextual_evidence':claims})
        # Some genuinely newer protocol discoveries exist only in technical documents.
        if ident not in grouped and not any(o['path'].startswith(('devices/','protocols/','functions/','registry/FAST_','evidence/')) for o in occurrences.get(ident,[])):issue('unknown_claim_id',id=ident)
        for c in claims:
            if c['status'] not in STATUSES:issue('invalid_status',id=ident)
            if c['status']=='CONFIRMED' and not c.get('device'):issue('unscoped_confirmation',id=ident)
            for source in c['sources']:
                if not (root/source).is_file():issue('missing_claim_source',id=ident,path=source)
            if c['status']=='SUPERSEDED' and not c.get('superseded_by'):issue('missing_successor',id=ident)
    # Compatibility claims are reviewed separately from broad legacy matrix prose.
    contexts=collections.defaultdict(set)
    for ident,claims in decisions['contextual_evidence'].items():
        for c in claims:contexts[(ident,c.get('device'),c.get('firmware'),c.get('protocol'))].add(c['status'])
    for ctx,ss in contexts.items():
        if 'CONFIRMED' in ss and 'REJECTED' in ss:issue('compatibility_conflict',context=ctx,statuses=sorted(ss))
    result={'raw_rows':len(rows),'unique_ids':len(grouped),'text_files':len(texts),'files':len(inventory),
        'legacy_status_counts':dict(sorted(collections.Counter(r['Status'] for _,r in rows).items())),
        'findings':issues,'limitations':['Markdown links checked, not bare code paths or remote URLs.',
          'Semantic contradictions require human review; context equality is exact, not inferred.',
          'Legacy classification is conservative, not a new hardware verification.',
          'Source existence is checked; authenticity and cited content require review.']}
    return catalog,inventory,result,occurrences

def outputs(root=ROOT):
    catalog,inventory,result,occ=audit(root)
    index=['# Record occurrence index (generated)','','Generated by `python tools/kb/audit.py --write`. Locations are search hits, not independent evidence.','']
    for ident,hits in sorted(occ.items()):
        index+=['## '+ident,'']
        index += [f'- [{h["path"]}:{h["line"]}](../../{h["path"]})' for h in hits]
        index+=['']
    return {'registry/audit/catalog.json':dump(catalog),'registry/audit/inventory.json':dump(inventory),
        'registry/audit/findings.json':dump(result),'registry/audit/occurrences.md':'\n'.join(index)+'\n'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--check',action='store_true');a=ap.parse_args()
    out=outputs(); result=json.loads(out['registry/audit/findings.json']);counts=collections.Counter(i['kind'] for i in result['findings'])
    print(dump({k:result[k] for k in ['raw_rows','unique_ids','files','text_files']}));print(dump(dict(counts)))
    if a.write:
        for p,s in out.items():(ROOT/p).write_text(s)
    failures=[i for i in result['findings'] if i['kind'] not in {'missing_explicit_row_source','same_context_mechanism'}]
    if a.check:
        for p,s in out.items():
            if not (ROOT/p).exists() or (ROOT/p).read_text()!=s:failures.append({'kind':'stale_generated_file','path':p})
    if failures:print(dump(failures));return 1
    return 0
if __name__=='__main__':sys.exit(main())
