# VectorForge LotL Data Pack

> **Scope:** Data sources only. Partners own lab setup, LotL generation, normalization, and any streaming/ingest.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://vectorforgeai.github.io/vectorforge-threat-telemetry/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?branch=main&label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

📖 **View Documentation:** https://vectorforgeai.github.io/vectorforge-threat-telemetry/

```mermaid
flowchart LR
  A[Sources] --> B[Mapping & Normalization]
  B --> C[VectorForge Ingest]

  subgraph Sources
    A1[Win Sec 4688/4689]
    A2[Sysmon 1/3/7/10/11/12–14/22]
    A3[PS 4104]
    A4[WMI 5857–5861]
    A5[BITS 59]
  end

  subgraph Mapping & Normalization
    M1[Field maps → VF schema (JSONL)]
    M2[PROVENANCE + hashes]
    M3[Link-check CI]
  end

  subgraph VectorForge Ingest
    V1[/workspace/<option>/*.jsonl]
    V2[workspace-manifest + hashes]
    V3[Quality checklist]
  end
