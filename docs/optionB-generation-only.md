# Option B — Generation‑only (your lab, your signals)

**Goal:** Generate LotL telemetry on your gold images and domain.

## Instrument
Enable 4688 with command line, PowerShell 4104, WMI‑Activity Operational, BITS Operational, and install Sysmon with a reputable config.

## Generate
- **Atomic Red Team** — run T1218 sub‑techniques (`regsvr32`, `rundll32`, `mshta`, `installutil`, `msiexec`, `cmstp`, `certutil`) + PowerShell/WMI/BITS atomics.
- **PurpleSharp** — playbooks across Windows/AD to light up Sysmon/Security/PowerShell logs.
- (Optional) **MITRE Caldera** — chain behaviors; export run logs.

## Collect
Use `scripts/export_win_events.ps1` (wrapper around OTRF Export‑WinEvents) to write **JSON** files for:
- `Security`, `Microsoft-Windows-Sysmon/Operational`, `Microsoft-Windows-PowerShell/Operational`,
  `Microsoft-Windows-WMI-Activity/Operational`, `Microsoft-Windows-BITS-Client/Operational`.

Store per scenario under `/delivery/optionB/<scenario>/`.

## Label
Fill `manifests/procedures.yaml` with ATT&CK IDs + LOLBAS entries used. Include exact start/stop timestamps and hostnames.

## Partner deliverables
- `/delivery/optionB/<scenario>/*.jsonl`
- `/delivery/optionB/<scenario>/labels.json`
- `/delivery/optionB/<scenario>/ingest-manifest.yaml`
- Completed `docs/acceptance-checklist.md`
