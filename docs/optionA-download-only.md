# Option A — Download‑only (Curated Seed)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://<org>.github.io/<repo>/)
[![Link Health](https://img.shields.io/github/actions/workflow/status/VectorForgeAI/vectorforge-threat-telemetry/link-check.yml?branch=main&label=link%20health)](https://github.com/VectorForgeAI/vectorforge-threat-telemetry/actions/workflows/link-check.yml)

**Goal:** Stand up LotL‑ready data fast using public datasets that already include Windows + Sysmon and realistic background noise.

**Who is this for?** Teams that need data immediately and do not have a lab environment for custom signal generation.

### Datasets (Use All Three)

1.  **Splunk BOTS v3 (pre‑indexed):** Includes `wineventlog` and `xmlwineventlog:microsoft-windows-sysmon/operational` data. Download from Splunk’s S3 and verify the MD5.
2.  **Security‑Datasets (OTRF):** Select Windows datasets aligned to LOLBAS/ATT&CK.
3.  **LANL Unified Host & Network:** Adds enterprise-scale host and netflow data with 4688/4689 events present.

### Steps

1.  **Fetch Public Datasets**
    This script reads from `manifests/datasets.yaml`, downloads the datasets, and writes hashes.
    ```bash
    python scripts/fetch_datasets.py
    ```

2.  **Export BOTS v3 Data from Splunk**
    The BOTS data must be exported from a Splunk instance. We recommend using Docker for this.
    * **Deploy Splunk:**
        ```bash
        docker run -d -p 8000:8000 -p 8089:8089 \
        -e "SPLUNK_START_ARGS=--accept-license" \
        -e "SPLUNK_PASSWORD=yourSecurePassword" \
        --name splunk splunk/splunk:latest
        ```
    * **Install the App:** Log in to Splunk, go to Apps -> Manage Apps, and install the downloaded BOTSv3 app.
    * **Run the Export:** The one-liner in `scripts/splunk_export_botsv3.md` exports only `wineventlog` and Sysmon data to JSON for VF.

3.  **Normalize Data to VF Schema**
    Apply the provided field mappings to convert the source JSON into the standardized JSONL format required by VF. Output the files to `/delivery/optionA/`.
    ```bash
    # Example command
    python scripts/normalize.py --mapping manifests/field-mapping-splunk.yml --input botsv3.json --output /delivery/optionA/botsv3.jsonl
    ```

4.  **Package for Delivery**
    Create the manifest file from the template and generate checksums for your final `.jsonl` files.
    ```bash
    sha256sum /delivery/optionA/*.jsonl > /delivery/optionA/hashes.txt
    ```

### Partner Deliverables

* `/delivery/optionA/*.jsonl` (chunked by source)
* `/delivery/optionA/ingest-manifest.yaml` (completed)
* `/delivery/optionA/hashes.txt` (MD5/SHA256)
* Completed `docs/acceptance-checklist.md`
