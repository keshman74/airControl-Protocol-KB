"""Regression checks for actual audit behavior, using isolated repository fixtures."""
import csv, json, tempfile, unittest
from pathlib import Path
from audit import audit, status

class AuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.root=Path(self.tmp.name)
        (self.root/'registry/records').mkdir(parents=True);(self.root/'protocols/test').mkdir(parents=True)
        (self.root/'registry/KB_DECISIONS.json').write_text(json.dumps({'duplicate_ids':{},'contextual_evidence':{}}))
        self.row={'ID':'CMD-TEST-ONE','Family':'test','Device':'A31','Function':'volume','Protocol':'HTTP80',
                  'Command / mechanism':'volume:10','Status':'DOCUMENTED','Response / notes':''}
        self.rows([self.row]);(self.root/'protocols/test/COMMANDS.md').write_text('# CMD-TEST-ONE\n')
    def rows(self,rows):
        with (self.root/'registry/records/test.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(self.row));w.writeheader();w.writerows(rows)
    def kinds(self):return {i['kind'] for i in audit(self.root)[2]['findings']}
    def test_duplicate_id_fails_without_exception(self):
        self.rows([self.row,self.row]);self.assertIn('duplicate_id',self.kinds())
    def test_cross_device_same_text_not_duplicate(self):
        other=dict(self.row,ID='CMD-TEST-TWO',Device='A33');self.rows([self.row,other])
        self.assertNotIn('same_context_mechanism',self.kinds())
    def test_same_context_different_ids_is_candidate(self):
        self.rows([self.row,dict(self.row,ID='CMD-TEST-TWO')]);self.assertIn('same_context_mechanism',self.kinds())
    def test_links_and_fences(self):
        (self.root/'README.md').write_text('[missing](absent.md)\n```md\n[example](template.md)\n```\n')
        issues=audit(self.root)[2]['findings'];links=[i for i in issues if i['kind']=='broken_link']
        self.assertEqual([i['target'] for i in links],['absent.md'])
    def test_anchor_check(self):
        (self.root/'README.md').write_text('[good](protocols/test/COMMANDS.md#cmd-test-one) [bad](protocols/test/COMMANDS.md#missing)')
        self.assertIn('broken_anchor',self.kinds())
    def test_no_hardware_promotion_from_code_or_capture(self):
        for s in ['IMPLEMENTED','CAPTURED','IMPLEMENTED/NEEDS-HW-EVIDENCE','DOCUMENTED / NOT-YET-HW-VERIFIED','APK-VERIFIED / NOT-HW-VERIFIED']:
            self.assertNotEqual(status(s),'CONFIRMED')
    def test_scoped_conflict_and_missing_source(self):
        d={'duplicate_ids':{},'contextual_evidence':{'CMD-TEST-ONE':[
           dict(device='A31',firmware='v1',protocol='HTTP80',status=s,sources=['absent.md']) for s in ['CONFIRMED','REJECTED']]}}
        (self.root/'registry/KB_DECISIONS.json').write_text(json.dumps(d))
        self.assertTrue({'compatibility_conflict','missing_claim_source'}<=self.kinds())
    def test_changed_device_not_false_conflict(self):
        d={'duplicate_ids':{},'contextual_evidence':{'CMD-TEST-ONE':[
          dict(device=device,firmware='unknown',protocol='HTTP80',status=s,sources=['protocols/test/COMMANDS.md'])
          for device,s in [('A97','REJECTED'),('A98','CONFIRMED')]]}}
        (self.root/'registry/KB_DECISIONS.json').write_text(json.dumps(d));self.assertNotIn('compatibility_conflict',self.kinds())
    def test_superseded_needs_successor(self):
        d={'duplicate_ids':{},'contextual_evidence':{'CMD-TEST-ONE':[dict(device='A31',firmware='unknown',protocol='HTTP80',status='SUPERSEDED',sources=['protocols/test/COMMANDS.md'])]}}
        (self.root/'registry/KB_DECISIONS.json').write_text(json.dumps(d));self.assertIn('missing_successor',self.kinds())
if __name__=='__main__':unittest.main()
