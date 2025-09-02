# Exporting BOTS v3 Windows + Sysmon from Splunk

1) Install Splunk; unpack BOTS v3 into `$SPLUNK_HOME/etc/apps`; restart.  
2) Export just Windows logs + Sysmon:

```bash
curl -k -u admin:changeme "https://localhost:8089/services/search/jobs/export" -d search='search index=botsv3 (sourcetype=wineventlog OR sourcetype="xmlwineventlog:microsoft-windows-sysmon/operational") earliest=0' -d output_mode=json > botsv3-windows-sysmon.json
```

3) Run the field mapping (`manifests/field-mapping-splunk.yml`) and write JSONL to `/workspace/optionA/`.
