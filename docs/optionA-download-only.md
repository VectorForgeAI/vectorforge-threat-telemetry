# Option A — Download‑only (curated seed)

**Goal:** Stand up LotL‑ready data fast using public datasets that already include Windows + Sysmon and realistic background.

## Datasets (use all three)
1) **Splunk BOTS v3 (pre‑indexed)** — CC0; includes `wineventlog` and `xmlwineventlog:microsoft-windows-sysmon/operational`. Download from Splunk’s S3 and verify MD5.  
2) **Security‑Datasets (OTRF)** — MIT; select Windows datasets aligned to LOLBAS/ATT&CK. Use their Export‑WinEvents approach to keep JSON portable.  
3) **LANL Unified Host & Network** — CC0; adds enterprise‑scale host + netflow with **4688/4689** present.

## Steps
1. **Pull datasets via `scripts/fetch_datasets.py`** — fetch CC0/MIT sets and write hashes to `manifests/datasets.yaml`.
2. **BOTS v3 export** — deploy local Splunk (free), add the pre‑indexed app, then run the one‑liner in `scripts/splunk_export_botsv3.md` to export **only** `wineventlog` + Sysmon to JSON for VF.
3. **Normalize** — apply `manifests/field-mapping-splunk.yml` and `field-mapping-winevent.yml`. Output **JSONL** to `/delivery/optionA/`.
4. **Package** — create `/delivery/optionA/ingest-manifest.yaml` (template in `templates/`). Include `hashes.txt` and dataset citations.

## Partner deliverables
- `/delivery/optionA/*.jsonl` (chunked by source)
- `/delivery/optionA/ingest-manifest.yaml` (completed)
- `/delivery/optionA/hashes.txt` (MD5/SHA256)
- Completed `docs/acceptance-checklist.md`
