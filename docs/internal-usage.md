# How to Use These Data Sources Internally

> **Scope:** We provide curated sources, schema, and QA. You assemble a **working set** for internal analysis and detection.

## Steps
1. Pick **Option A** (download), **B** (generate), or **C** (hybrid).
2. Normalize records to **JSONL** with VF fields:
   `time, host, user, ch, event_id, image, command_line, parent_image, parent_cmd, hashes, signed_status, dest_ip, dest_port, dns_query, registry_key`
3. Place outputs under **/workspace/<option>/** (examples below).
4. Add:
   - **workspace-manifest.yaml** (counts per file/channel)
   - **PROVENANCE.txt** (licensing + hashes per source)
   - **hashes.txt** (MD5 + SHA256 for every artifact)
5. Run your QA (and/or `scripts/qa_jsonl.py`) until the **Quality Checklist** is 100% green.

### Folder examples
- `/workspace/optionA/*.jsonl`
- `/workspace/optionB/<scenario>/*.jsonl`
- `/workspace/optionC/{botsv3,otrf,lab}/*.jsonl`

### Hashing quick refs
**macOS/Linux**
```bash
md5sum file.ext >> hashes.txt
shasum -a 256 file.ext >> hashes.txt
```

**Windows PowerShell**
```powershell
Get-FileHash .\file.ext -Algorithm MD5    | % { "$($_.Hash)  file.ext" }     >> hashes.txt
Get-FileHash .\file.ext -Algorithm SHA256 | % { "$($_.Hash)  file.ext" }     >> hashes.txt
```

### Quality checklist (pass/fail)
- JSONL parses (no invalid lines)
- Required fields present (see schema)
- Hashes recorded for each artifact (MD5 + SHA256)
- **PROVENANCE.txt** completed for each source
