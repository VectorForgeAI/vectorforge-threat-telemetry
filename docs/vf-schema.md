# VF Ingest Schema (minimum fields)

| Field            | Source examples                                      |
|------------------|-------------------------------------------------------|
| time             | Event timestamp (UTC ISO8601)                         |
| host             | Computer/LogHost                                      |
| user             | UserName/SubjectUserName                              |
| ch               | Channel/Sourcetype (security, sysmon, powershell, …) |
| event_id         | 4688, 4104, 5857, 59, 1, 3, 22, …                     |
| image            | Process/Image                                         |
| command_line     | CommandLine                                           |
| parent_image     | ParentProcessName/Image                               |
| parent_cmd       | ParentCommandLine                                     |
| hashes           | Sysmon (SHA1/SHA256/IMPHASH)                          |
| signed_status    | Sysmon Signed/Signer                                  |
| dest_ip/port     | Sysmon 3                                              |
| dns_query        | Sysmon 22                                             |
| registry_key     | Sysmon 12–14                                          |

**Mappings included:**  
- `manifests/field-mapping-splunk.yml` (BOTS v3 → VF)  
- `manifests/field-mapping-winevent.yml` (native EVTX/JSON → VF)
