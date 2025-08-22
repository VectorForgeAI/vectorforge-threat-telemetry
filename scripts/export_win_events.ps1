# Thin wrapper: export key channels to JSON (uses OTRF Export‑WinEvents)
# Requires the Export-WinEvents module installed in the session.
param(
  [string]$OutputFolder = "C:\vf_out",
  [string]$TimeBucket = "Last 24 Hours"
)

$channels = @(
  'Security',
  'Microsoft-Windows-Sysmon/Operational',
  'Microsoft-Windows-PowerShell/Operational',
  'Microsoft-Windows-WMI-Activity/Operational',
  'Microsoft-Windows-BITS-Client/Operational'
)

New-Item -ItemType Directory -Path $OutputFolder -Force | Out-Null

foreach ($c in $channels) {
  try {
    $null = $c | Export-WinEvents -TimeBucket $TimeBucket -OutputFolder $OutputFolder -Verbose
  } catch {
    Write-Warning "Failed exporting $c: $($_.Exception.Message)"
  }
}
