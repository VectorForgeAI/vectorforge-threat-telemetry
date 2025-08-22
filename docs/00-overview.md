# VF LotL Data Pack — Overview
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://<org>.github.io/<repo>/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?branch=main&label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

This repository provides three proven paths to deliver Living off the Land (LotL) telemetry into VectorForge (VF).

* **Option A — Download‑only:** Seed with public, LotL‑relevant data (Windows + Sysmon).
* **Option B — Generation‑only:** Generate LotL in your own lab, then export Windows/Sysmon/PowerShell/WMI/BITS.
* **Option C — Hybrid:** Seed and generate data for fast coverage and environment realism.

### What VF expects (schema‑level signals)

VF's analytics engine requires specific event types to model LotL behavior. Your final data must contain these key signals:

| Event ID / Source | Type | Why It Matters for LotL Detection |
| :--- | :--- | :--- |
| **Windows Security 4688/4689** | Process Auditing | The cornerstone of process tracking. The `CommandLine` field is mandatory. |
| **Windows Security 4624/4625, 4648, 4672**| Logon Auditing | Tracks successful/failed logons, "Run as" events, and special privilege assignments. |
| **PowerShell 4104** | Script Block Logging | Captures de-obfuscated script content, exposing malicious commands. |
| **WMI‑Activity 5857–5861** | WMI Auditing | Logs WMI permanent event subscriptions, a common persistence technique. |
| **BITS‑Client/Operational 59** | BITS Auditing | Tracks the creation of BITS jobs, which can be used to download payloads covertly. |
| **Sysmon 1,3,7,10,11,12–14,22** | Core Telemetry | Provides deep visibility into process creation, network connections, process injection, registry modifications, and DNS queries. |

### What We Provide

This repository is a self-contained toolkit to help your team succeed.

* A **datasets manifest** with links, hashes, and licenses.
* **Field mappings** to translate raw log fields into VF’s schema.
* **Scripts** to automate fetching, converting, and exporting data.
* A strict **acceptance checklist** for self-validating your work before delivery.
