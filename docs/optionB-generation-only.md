# Option B — Generation-only (Your Lab, Your Signals)

**Goal:** Generate LotL telemetry on your gold images and domain.

**Who is this for?** Teams with a lab environment who need to validate detections against their specific security tooling and configurations.

---

### 1. Instrument Your Lab
Ensure your Windows hosts are configured to generate the required logs.

- **Enable Process Creation Auditing (4688):** Use Group Policy or `auditpol.exe`. You must enable "Include command line in process creation events".
- **Enable PowerShell ScriptBlock Logging (4104):** Enable via Group Policy to capture full script contents.
- **Enable WMI & BITS Logging:** In Event Viewer, enable the `Operational` logs for `WMI-Activity` and `BITS-Client`.
- **Install and Configure Sysmon:** Install Sysmon with a reputable configuration file (e.g., from SwiftOnSecurity) to generate detailed telemetry.

---

### 2. Generate LotL Activity
Run attack simulation tools to generate telemetry.

- **Atomic Red Team:** Execute discrete, ATT&CK-mapped tests for LOLBAS techniques like `regsvr32`, `rundll32`, `mshta`, `certutil`, etc.
- **PurpleSharp:** Simulate adversary behaviors across a Windows Active Directory environment to generate logs.

---

### 3. Collect Logs
Use the provided `scripts/export_win_events.ps1` script to export event logs to JSON files.  
This script is a wrapper around the OTRF Export-WinEvents tool.

```powershell
# Run this on the target machine
.\scripts\export_win_events.ps1 -ScenarioName "T1218_Regsvr32" -OutputDir "/delivery/optionB/T1218_Regsvr32/"
```

---

### 4. Label Your Data
This step is critical for generated data.  
Fill out `manifests/procedures.yaml` with the ATT&CK IDs, LOLBAS entries, start/stop timestamps, and hostnames for your simulation.

---

### Partner Deliverables
- `/delivery/optionB/<scenario>/*.jsonl`
- `/delivery/optionB/<scenario>/labels.json`
- `/delivery/optionB/<scenario>/ingest-manifest.yaml`

---

### Completed
- `docs/acceptance-checklist.md`
