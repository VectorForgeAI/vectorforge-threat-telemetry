# ⚡ VectorForge Threat Telemetry

_A curated data pack for Living-off-the-Land (LotL) detection and validation._

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://vectorforgeai.github.io/vectorforge-threat-telemetry/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

![VectorForge LotL Data Pack](../assets/cover.png)

### The Challenge of LotL

Detecting adversaries who use a system's own legitimate tools to execute their mission—a technique known as **Living-off-the-Land (LotL)**—is a fundamental challenge for modern security teams. These attacks blend in with normal administrative activity, making them difficult to isolate and identify. Effective detection engineering for LotL requires high-quality, realistic telemetry that mirrors these subtle behaviors.

This project provides a curated data pack and a set of methodologies to generate and deliver that crucial telemetry into VectorForge.

---

### Three Paths to High-Fidelity Data

We offer three distinct paths to acquire the data you need. Choose the one that best fits your timeline, resources, and desired level of environmental realism.

-   **Option A — Download-only:** The fastest path to get started. Seed your environment with trusted public datasets that already contain a rich mix of Windows and Sysmon events.

-   **Option B — Generation-only:** The highest-fidelity approach. Generate LotL telemetry within your own lab environment, using your gold images and security configurations.

-   **Option C — Hybrid:** The recommended approach for most teams. Combine the speed of public datasets with the realism of targeted, lab-generated events for the best of both worlds.

---

### Getting Started

We've designed this repository to be a complete toolkit. Follow these steps to begin:

1.  **Understand the Core Concepts:** Read the [Overview](00-overview.md) to learn about the specific event logs and signals VectorForge expects.

2.  **Choose Your Delivery Path:** Select your preferred method: [Option A](optionA-download-only.md), [Option B](optionB-generation-only.md), or [Option C](optionC-hybrid.md).

3.  **Review the Data Requirements:** Familiarize yourself with the target [VF Ingest Schema](vf-schema.md) and the approved [Data Sources](data-sources.md).

4.  **Validate Your Results:** Before finalizing your delivery, use the [Acceptance Checklist](acceptance-checklist.md) to ensure your data meets all quality standards.

---

### Integrity & Licensing
We link to canonical sources (Splunk BOTSv3, LANL UH&N, OTRF Security‑Datasets). CC0 datasets may be mirrored for offline use; we preserve hashes and citations in manifests.
