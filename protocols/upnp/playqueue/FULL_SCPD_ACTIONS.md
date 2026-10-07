# PlayQueue full SCPD inventory — CHAT-AUDIT-02

A later full sweep of `wiim-playback-map.txt` exposed the embedded PlayQueue
SCPD in `vt1.java`. This materially expands the previously known 4-action set.

Key families:
- queue lifecycle: CreateQueue, ReplaceQueue, DeleteQueue, BackUpQueue, AppendQueue
- browsing: BrowseQueue, BrowseQueueEx
- playback/policy: PlayQueueWithIndex, Set/GetQueueLoopMode, SetQueuePolicy
- track editing: AppendTracksInQueue, AppendTracksInQueueEx, RemoveTracksInQueue
- online-service operations: GetQueueOnline, SearchQueueOnline, SetRating,
  StreamSetQuality/StreamGetQuality
- presets/key mapping: SetKeyMapping/GetKeyMapping
- account/session surface: UserRegister, UserLogin, UserLogout
- record/favorite-like operations: SetQueueRecord, SetSongsRecord

Security note: UserLogin includes password, authorization code, code verifier,
token and proxy fields. KB must preserve the schema but never capture real
credentials.

This is SCPD/source evidence. It does NOT mean every action is implemented by
every A31/A97/A98 firmware. Runtime service/action discovery and hardware tests
remain authoritative.
