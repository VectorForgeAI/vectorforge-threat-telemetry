# Caldera LotL Simulation Assets

**Scope:** Example **data-generation** assets. You run these in your own lab to produce Windows telemetry (Security, Sysmon, PowerShell 4104, WMI 5857–5861, BITS 59).  
**Repo scope remains data-sources only**—you own setup, execution, and normalization.

## What's here

```
caldera/
├── adversary-lotl.yml          # Chained regsvr32 -> mshta -> BITS -> WMI
└── abilities/
    ├── T1218.011_regsvr32.yml
    ├── T1218.001_mshta.yml
    ├── T1197_BITS_job.yml
    └── T1047_WMI_exec.yml
```

## Quickstart (Caldera)
1. **Controller running** (Docker or host).  
2. **Agent on Windows victim** (sandcat).  
3. **Import adversary:** Caldera UI → *Adversaries* → **Import from YAML** → select `adversary-lotl.yml`.  
4. **Run operation:** *Operations* → **New** → pick **VF LotL Chain** → select your agent/group → **Run**.  
   - Note **start/stop** times for provenance.

## Expected signals
- **T1218.* (regsvr32/mshta):** Security **4688** (+CommandLine), Sysmon **1**, optional **3/22**.  
- **T1197 (BITS):** BITS-Client/Operational **59** (+4688/Sysmon 1 parent).  
- **T1047 (WMI):** WMI-Activity/Operational **5857–5861** (+4688/Sysmon 1).

## Export & organize (internal use)
- Export logs:
  ```powershell
  .\scripts\export_win_events.ps1 -OutputFolder .\workspace\optionB\run_01 -TimeBucket "Last 2 Hours"
  ```

Place results under:
```
/workspace/optionB/run_01/*.json
/workspace/optionB/run_01/PROVENANCE.txt
/workspace/optionB/run_01/workspace-manifest.yaml
/workspace/optionB/run_01/hashes.txt
```

## Customize safely
- Replace external URLs in abilities (e.g., BITS source) with benign internal endpoints.
- Executors are defined (cmd, psh) with timeouts—adjust as needed.
- Keep commands benign; goal is to light up telemetry, not execute malware.

## Safety
- Lab-only. Use NAT networking, snapshots, and your org's policies. Do not run in production.

## Provenance
- Complete PROVENANCE.txt for each working set (sources, licenses, hashes, timestamps). See templates in `/templates/`.
