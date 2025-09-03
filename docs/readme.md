![VectorForge LotL Data Pack](../assets/cover.png)

# VectorForge LotL Data Pack

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://vectorforgeai.github.io/vectorforge-threat-telemetry/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?branch=main&label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

**Three workspace paths for Living‑off‑the‑Land (LotL) telemetry into VectorForge**

- **Option A — Download-only:** Seed with public datasets (Windows + Sysmon).
- **Option B — Generation-only:** Generate LotL in your lab; export Windows/Sysmon/PowerShell/WMI/BITS.
- **Option C — Hybrid:** Seed + generate for fast coverage *and* environment realism.

## Start here
- **How to use internally:** see [internal-usage.md](internal-usage.md)
- Templates: see [/templates](../templates/)
- **Simulate LotL with Caldera:** see [simulate-lotl-caldera.md](simulate-lotl-caldera.md) and [caldera assets](../caldera/)
- Read the [Overview](00-overview.md)
- Pick an option: [A](optionA-download-only.md), [B](optionB-generation-only.md), or [C](optionC-hybrid.md)
- Validate with the [Acceptance Checklist](acceptance-checklist.md)
- See [VF Ingest Schema](vf-schema.md) and [Data Sources](data-sources.md)

---

### Integrity & Licensing
We link to canonical sources (Splunk BOTSv3, LANL UH&N, OTRF Security‑Datasets). CC0 datasets may be mirrored for offline use; we preserve hashes and citations in manifests.