# StoryScript User Uninstaller (No Admin Required!)

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   StoryScript User Uninstaller" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$installDir = "$env:LOCALAPPDATA\StoryScript"

Write-Host "Removing StoryScript from: $installDir" -ForegroundColor Yellow
Write-Host ""

# Remove from USER PATH
Write-Host "[1/4] Removing from your PATH..." -ForegroundColor Green
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
$newPath = ($currentPath.Split(';') | Where-Object { $_ -ne $installDir }) -join ';'
[Environment]::SetEnvironmentVariable("Path", $newPath, "User")
Write-Host "    Removed from PATH" -ForegroundColor Gray

# Remove installation directory
Write-Host "[2/4] Removing installation files..." -ForegroundColor Green
if (Test-Path $installDir) {
    Remove-Item -Path $installDir -Recurse -Force
    Write-Host "    Files removed" -ForegroundColor Gray
}

# Remove Start Menu shortcuts
Write-Host "[3/4] Removing Start Menu shortcuts..." -ForegroundColor Green
$startMenuDir = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\StoryScript"
if (Test-Path $startMenuDir) {
    Remove-Item -Path $startMenuDir -Recurse -Force
    Write-Host "    Shortcuts removed" -ForegroundColor Gray
}

# Remove file association
Write-Host "[4/4] Removing file associations..." -ForegroundColor Green
$userClasses = "HKCU:\Software\Classes"
if (Test-Path "$userClasses\.story") {
    Remove-Item -Path "$userClasses\.story" -Recurse -Force
    Write-Host "    .story extension removed" -ForegroundColor Gray
}
if (Test-Path "$userClasses\StoryScript.File") {
    Remove-Item -Path "$userClasses\StoryScript.File" -Recurse -Force
    Write-Host "    StoryScript file type removed" -ForegroundColor Gray
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Uninstallation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "StoryScript has been removed from your account." -ForegroundColor Cyan
Write-Host ""
Write-Host "You may need to:" -ForegroundColor Yellow
Write-Host "  • Close and reopen command prompts" -ForegroundColor White
Write-Host "  • Refresh File Explorer (F5)" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to finish"
