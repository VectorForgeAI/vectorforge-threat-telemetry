# Option C — Hybrid (seed + top‑off)

**Goal:** Deliver breadth immediately, then personalize with your lab’s LotL.

## Do this
1) **Seed:** Import/export **BOTS v3** Windows + Sysmon to JSONL.  
2) **Add:** Pull 3–5 **Security‑Datasets** Windows scenarios that cover LOLBAS techniques you care about.  
3) **Top‑off:** Run T1218 + WMI + BITS atomics in your lab and export logs via `export_win_events.ps1`.  
4) **Normalize:** Map everything to `docs/vf-schema.md`; package under `/workspace/optionC/`.

## Partner deliverables
- `/workspace/optionC/{botsv3,otrf,lab}/*.jsonl`
- Combined `/workspace/optionC/workspace-manifest.yaml` + `hashes.txt`
- Completed `docs/acceptance-checklist.md`
