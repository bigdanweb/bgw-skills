# Links every skill and the output styles into ~/.claude, and copies the global CLAUDE.md.
$ErrorActionPreference = "Stop"
$repo = $PSScriptRoot
$claude = Join-Path $HOME ".claude"
$skills = Join-Path $claude "skills"
$backup = Join-Path $claude ("bgw-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss"))

function Set-Junction($link, $target) {
    $existing = Get-Item $link -ErrorAction SilentlyContinue
    if ($existing -and $existing.LinkType -eq "Junction") {
        $existing.Delete()
    } elseif ($existing) {
        New-Item -ItemType Directory -Force $backup | Out-Null
        Move-Item $link (Join-Path $backup (Split-Path $link -Leaf))
    }
    New-Item -ItemType Junction -Path $link -Target $target | Out-Null
    "linked $(Split-Path $link -Leaf)"
}

New-Item -ItemType Directory -Force $skills | Out-Null
foreach ($skill in Get-ChildItem (Join-Path $repo "skills") -Directory) {
    Set-Junction (Join-Path $skills $skill.Name) $skill.FullName
}
Set-Junction (Join-Path $claude "output-styles") (Join-Path $repo "output-styles")

$target = Join-Path $claude "CLAUDE.md"
if (Test-Path $target) {
    New-Item -ItemType Directory -Force $backup | Out-Null
    Copy-Item $target (Join-Path $backup "CLAUDE.md")
}
Copy-Item (Join-Path $repo "claude\CLAUDE.md") $target
"copied CLAUDE.md"
if (Test-Path $backup) { "replaced files are in $backup" }
