# Simulate LotL with MITRE Caldera (Quickstart)

> **Safety & Scope**
> - Lab-only; never run in production.
> - Replace external URLs with your internal benign host.
> - Keep egress blocked/controlled; use NAT + snapshots.
> - You are responsible for complying with your org's policies.

> **Lab-only.** Partners run this in an isolated Windows lab to produce Windows Security, Sysmon, PowerShell 4104, WMI (5857–5861), and BITS (59) signals.

## Why use Caldera here
- Chain multiple LotL techniques in one operation (repeatable, multi-step)
- Save/replay profiles to generate consistent telemetry across runs/hosts

## Minimal flow
1) Start the Caldera controller (Docker or host install).
2) On your Windows victim, run the Caldera agent (sandcat).
3) Import the example adversary profile from `/caldera/adversary-lotl.yml`.
4) Execute the operation and note start/stop times for provenance.

## Expected signals by step
- **T1218.* (regsvr32 / mshta / rundll32):** Security 4688 (+ CommandLine), Sysmon 1; optionally Sysmon 3/22 if network touched.
- **T1197 (BITS):** BITS-Client/Operational 59 (+ 4688 / Sysmon 1 parent).
- **T1047 (WMI):** WMI-Activity/Operational 5857–5861 (+ 4688 / Sysmon 1).

## Export and organize (internal use)
- Export key channels with our wrapper:
  ```powershell
  .\scripts\export_win_events.ps1 -OutputFolder .\workspace\optionB\run_01 -TimeBucket "Last 2 Hours"
  ```
- Place outputs under:
  ```
  /workspace/optionB/run_01/*.json
  /workspace/optionB/run_01/PROVENANCE.txt
  /workspace/optionB/run_01/workspace-manifest.yaml
  /workspace/optionB/run_01/hashes.txt
  ```
- Fill **PROVENANCE.txt** (template in `/templates/`) and update **workspace-manifest.yaml** (example in `/templates/`).
- (Optional) Convert to JSONL and run `scripts/qa_jsonl.py`.

## Notes
- Commands in the example abilities are benign placeholders; partners may substitute safe internal endpoints/paths.
- This repository remains **data-sources only**. Partners own lab setup, execution, and normalization.
