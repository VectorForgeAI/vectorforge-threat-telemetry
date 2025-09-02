# Data-sources Quickstart

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://<org>.github.io/<repo>/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?branch=main&label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

## What we provide
- Curated links to public datasets
- Field schema (VF minimum)
- Mapping examples and packaging rules
- Acceptance checklist

## What you (partner) do
- Download/Generate data
- Verify hashes, complete citations
- Normalize to VF schema (JSONL)
- Package under `/delivery/<option>`

## Steps
1) Pick Option A (download), B (generate), or C (hybrid).
2) For every dataset: compute MD5/SHA256 and add to `manifests/datasets.yaml`.
3) Normalize to JSONL fields: `time`, `host`, `user`, `ch`, `event_id`, `image`, `command_line`, `parent_image`, `parent_cmd`, `hashes`, `signed_status`, `dest_ip`, `dest_port`, `dns_query`, `registry_key`.
4) Create `/delivery/<option>/ingest-manifest.yaml` and `CITATIONS.txt`.
5) Run `scripts/qa_jsonl.py` locally; resolve any errors.
6) Submit the bundle when **acceptance-checklist.md** is 100% green.

## Quick Reference

### Required JSONL Fields
See [VF Schema](vf-schema.md) for complete field definitions and examples.

### Dataset Options
- **[Option A: Download-only](optionA-download-only.md)** — Use curated public datasets
- **[Option B: Generation-only](optionB-generation-only.md)** — Generate custom data
- **[Option C: Hybrid](optionC-hybrid.md)** — Combine both approaches

### Key Files
- `manifests/datasets.yaml` — Dataset metadata and hashes
- `templates/ingest-manifest.yaml` — Delivery manifest template
- `docs/acceptance-checklist.md` — Final validation checklist
- `manifests/field-mapping-*.yml` — Schema mapping examples

### Validation
Before submission, ensure your JSONL files contain:
- Windows Event ID 4688 with command line for LotL processes
- PowerShell 4104 events for script activity  
- WMI-Activity 5857–5861 where WMI is used
- BITS-Client 59 where BITS is used
- Sysmon 1,3,22 correlating with process + DNS/network activity
