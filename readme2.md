# ⚡ VectorForge Threat Telemetry

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://vectorforgeai.github.io/vectorforge-threat-telemetry/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

> Curated and lab-generated telemetry for Living-off-the-Land (LotL) techniques. Includes Windows Security events, Sysmon, and PowerShell. All data mapped to MITRE ATT&CK.

![VectorForge LotL Data Pack](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/raw/main/assets/flow.png)

This repository provides a curated data pack and methodologies to generate and deliver crucial Living-off-the-Land (LotL) telemetry into VectorForge. It is designed to help security teams test, validate, and improve their detection capabilities.

### Table of Contents
- [🚀 Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Three Paths to Telemetry](#three-paths-to-telemetry)
- [Use Cases](#use-cases)
- [Dataset Index](#dataset-index)
- [🤝 Contributing](#contributing)
- [Verify Downloads](#verify-downloads)

---

### 🚀 Getting Started

Follow these steps to begin using the VectorForge LotL Data Pack:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/VectorForgeAI/vectorforge-threat-telemetry.git](https://github.com/VectorForgeAI/vectorforge-threat-telemetry.git)
    cd vectorforge-threat-telemetry
    ```
2.  **Review the Documentation**
    Read the [Overview in our docs](docs/00-overview.md) to understand the core concepts and data schemas.

3.  **Choose Your Path**
    Select the delivery path (Option A, B, or C) that best fits your needs and follow the detailed instructions in its respective guide.

### Prerequisites

Before using the automation scripts, please ensure you have the following installed:
- Python 3.8+
- Docker (Required for Option A)
- Git

### Three Paths to Telemetry

We offer three distinct paths to acquire the data you need:

* **Option A — Download-only:** The fastest path to get started. Seed your environment with trusted public datasets that already contain a rich mix of Windows and Sysmon events.
* **Option B — Generation-only:** The highest-fidelity approach. Generate LotL telemetry within your own lab environment, using your gold images and security configurations.
* **Option C — Hybrid:** The recommended approach for most teams. Combine the speed of public datasets with the realism of targeted, lab-generated events.

### Use Cases

This project is designed for:
- **Detection Engineers:** Validate and test new detection rules for your SIEM or EDR.
- **Security Researchers:** Analyze adversary tradecraft using realistic event logs.
- **SOC Analysts & Threat Hunters:** Train with high-quality data to recognize subtle signs of LotL activity.

### Dataset Index

The following datasets are used or referenced in this project:

| Dataset Index | License | Link | Size | Ready/Verify |
| :--- | :--- | :--- | :--- | :--- |
| Splunk BOTSv3 | CC0 | [Official / Repo](https://github.com/splunk/botsv3) | Varies | Pre-indexed, requires export |
| LANL UH&N | CC0 | [Official / Repo](https://csr.lanl.gov/data/2017/) | 12GB | JSON/CSV |
| Mordor | GPL-3.0 | [Official / Repo](https://github.com/UraSecTeam/mordor) | Varies | JSON, EVTX |
| OTRF Security-Datasets| MIT | [Official / Repo](https://github.com/OTRF/Security-Datasets) | Varies | EVTX, requires export |
| LOLBAS | GPL-3.0 | [Official / Repo](https://github.com/LOLBAS-Project/LOLBAS) | <1MB | N/A (Reference) |

### 🤝 Contributing

We welcome contributions! Please read our `CONTRIBUTING.md` file to learn how you can report bugs, suggest features, or submit pull requests.

### Verify Downloads

Use `curl` or similar tools to verify dataset integrity using the hashes provided in the manifests.
```bash
# Example from the original README to verify a file
curl -L [https://example.com/botsv3_data.zip.md5](https://example.com/botsv3_data.zip.md5)
