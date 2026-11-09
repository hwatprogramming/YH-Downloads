# Checks every app's versions list (like yt-music-downloader\versions.js) against the
# files on GitHub, and says what's missing. check-versions.bat runs it.
#
# For each version in a list, it checks:
#   - its numbered copy is on GitHub, like yt-music-downloader-setup-1.1.0.exe
#   - the fixed name (yt-music-downloader-setup.exe) is the same size as the newest
#     numbered copy, so the download button gets the newest
# And it lists numbered copies on GitHub that the list doesn't have.
#
# It reads GitHub's public API, so it needs no login, only the internet.

$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$repo = 'hwatprogramming/YH-Downloads'
$problems = 0

function Bad($text) { Write-Host "  MISSING  $text" -ForegroundColor Red; $script:problems++ }
function Good($text) { Write-Host "  ok       $text" -ForegroundColor Green }

$lists = Get-ChildItem $PSScriptRoot -Directory |
  ForEach-Object { Join-Path $_.FullName 'versions.js' } |
  Where-Object { Test-Path $_ }

foreach ($list in $lists) {
  # The folder's name is the release's tag.
  $tag = Split-Path (Split-Path $list) -Leaf
  Write-Host ""
  Write-Host $tag

  # The list is plain JSON after "window.versions =".
  $text = Get-Content $list -Raw -Encoding UTF8
  $start = $text.IndexOf('{', $text.IndexOf('window.versions'))
  $versions = $text.Substring($start, $text.LastIndexOf('}') - $start + 1) | ConvertFrom-Json

  try {
    $release = Invoke-RestMethod "https://api.github.com/repos/$repo/releases/tags/$tag"
  } catch {
    Bad "no release called $tag on GitHub"
    continue
  }
  $files = @{}
  foreach ($a in $release.assets) { $files[$a.name] = $a.size }
  $listed = @{}

  foreach ($platform in $versions.PSObject.Properties) {
    $entries = @($platform.Value)
    foreach ($v in $entries) {
      if (-not $v.file -or -not $v.version) { Bad "$($platform.Name) $($v.version): its version or file is empty in the list"; continue }
      $listed[$v.file] = $true
      if ($files.ContainsKey($v.file)) { Good "$($platform.Name) $($v.version): $($v.file)" }
      else { Bad "$($platform.Name) $($v.version): $($v.file) isn't on GitHub" }
    }

    # The fixed name is the newest's file name without its number.
    $newest = $entries[0]
    if (-not $newest.file -or -not $newest.version) { continue }
    $fixed = $newest.file.Replace('-' + $newest.version, '')
    $listed[$fixed] = $true
    if (-not $files.ContainsKey($fixed)) {
      Bad "$($platform.Name): $fixed isn't on GitHub"
    } elseif (-not $files.ContainsKey($newest.file)) {
      # Its numbered copy is missing, already said above, so there's nothing to compare.
    } elseif ($files[$fixed] -ne $files[$newest.file]) {
      Bad "$($platform.Name): $fixed isn't the newest ($($newest.version)), its size is different"
    } else {
      Good "$($platform.Name): $fixed is $($newest.version)"
    }
  }

  foreach ($name in $files.Keys) {
    if (-not $listed.ContainsKey($name)) { Bad "$name is on GitHub but not in $tag\versions.js" }
  }
}

Write-Host ""
if ($problems -eq 0) { Write-Host "All good." -ForegroundColor Green }
else { Write-Host "$problems to fix." -ForegroundColor Red }
exit $problems
