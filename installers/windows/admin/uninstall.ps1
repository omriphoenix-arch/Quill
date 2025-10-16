# StoryScript Uninstaller for Windows

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   StoryScript Uninstaller" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check for admin rights
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This uninstaller requires administrator privileges!" -ForegroundColor Red
    Write-Host "Right-click PowerShell and select 'Run as Administrator', then try again." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

$installDir = "$env:ProgramFiles\StoryScript"

Write-Host "Removing StoryScript from: $installDir" -ForegroundColor Yellow
Write-Host ""

# Remove from PATH
Write-Host "[1/4] Removing from system PATH..." -ForegroundColor Green
$currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
$newPath = ($currentPath.Split(';') | Where-Object { $_ -ne $installDir }) -join ';'
[Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")

# Remove installation directory
Write-Host "[2/4] Removing installation files..." -ForegroundColor Green
if (Test-Path $installDir) {
    Remove-Item -Path $installDir -Recurse -Force
}

# Remove Start Menu shortcuts
Write-Host "[3/4] Removing Start Menu shortcuts..." -ForegroundColor Green
$startMenuDir = "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\StoryScript"
if (Test-Path $startMenuDir) {
    Remove-Item -Path $startMenuDir -Recurse -Force
}

# Remove file association
Write-Host "[4/4] Removing file associations..." -ForegroundColor Green
if (Test-Path "HKCR:\.story") {
    Remove-Item -Path "HKCR:\.story" -Force
}
if (Test-Path "HKCR:\StoryScript.File") {
    Remove-Item -Path "HKCR:\StoryScript.File" -Recurse -Force
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Uninstall Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "StoryScript has been removed from your system." -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to finish"
