# VF LotL Data Pack — Overview

This repo gives you three proven paths to deliver **Living off the Land (LotL)** telemetry into VectorForge (VF):
- **Option A — Download‑only:** Seed with public, LotL‑relevant data (Windows + Sysmon).
- **Option B — Generation‑only:** Generate LotL in your own lab, then export Windows/Sysmon/PowerShell/WMI/BITS.
- **Option C — Hybrid:** Seed + generate for fast coverage and environment realism.

**What VF expects (schema‑level signals):**
- Windows Security **4688/4689** (with command line), 4624/4625, 4648, 4672
- PowerShell **4104** (script block)
- WMI‑Activity **5857–5861**
- BITS‑Client/Operational (e.g., **59**)
- Sysmon **1,3,7,10,11,12–14,22**

We provide:
- A **datasets manifest** with links/hashes/licenses
- **Field mappings** to VF’s schema
- **Scripts** to fetch/convert/export
- A strict **acceptance checklist** so your team can validate their own work
