# Example: run a few ATT&CK T1218/WMI/BITS atomics (requires Invoke-AtomicRedTeam installed)
# Ensure you run in a LAB.
$tests = @(
  'T1218.011',  # regsvr32
  'T1218.010',  # rundll32
  'T1218.001',  # mshta
  'T1197',      # BITS jobs
  'T1047'       # WMI exec
)
foreach ($t in $tests) {
  try {
    Invoke-AtomicTest $t -GetPrereqs -Confirm:$false | Out-Null
    Invoke-AtomicTest $t -Confirm:$false
  } catch {
    Write-Warning "Failed atomic $t: $($_.Exception.Message)"
  }
}
