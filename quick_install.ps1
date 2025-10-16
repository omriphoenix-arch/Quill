# Quill One-Line Installer for Windows
# Usage: irm https://raw.githubusercontent.com/omriphoenix-arch/Quill/main/quick_install.ps1 | iex
# Or: powershell -ExecutionPolicy Bypass -File quick_install.ps1

param(
    [string]$InstallDir = "$env:USERPROFILE\quill"
)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Quill Quick Installer v1.0" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking for Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($pythonVersion -match "Python (\d+)\.(\d+)") {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 8)) {
            Write-Host "✗ Python 3.8+ required" -ForegroundColor Red
            Write-Host "  Download: https://www.python.org/downloads/" -ForegroundColor Yellow
            exit 1
        }
    }
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found" -ForegroundColor Red
    Write-Host "  Download: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Download
Write-Host "Downloading Quill (0.77 MB)..." -ForegroundColor Yellow
$tempZip = "$env:TEMP\quill-main.zip"
$url = "https://github.com/omriphoenix-arch/Quill/archive/refs/heads/main.zip"

try {
    Invoke-WebRequest -Uri $url -OutFile $tempZip -UseBasicParsing
    Write-Host "✓ Downloaded" -ForegroundColor Green
} catch {
    Write-Host "✗ Download failed" -ForegroundColor Red
    Write-Host "  Please check your internet connection" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Extract
Write-Host "Installing to $InstallDir..." -ForegroundColor Yellow
if (Test-Path $InstallDir) {
    Write-Host "  Removing previous installation..." -ForegroundColor Gray
    Remove-Item -Recurse -Force $InstallDir
}

New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null
Expand-Archive -Path $tempZip -DestinationPath $InstallDir -Force

# Move contents up one level (remove quill-main folder)
$extractedFolder = Get-ChildItem -Path $InstallDir -Directory | Select-Object -First 1
if ($extractedFolder) {
    Get-ChildItem -Path $extractedFolder.FullName | Move-Item -Destination $InstallDir -Force
    Remove-Item -Path $extractedFolder.FullName -Recurse -Force
}

Remove-Item -Path $tempZip -Force
Write-Host "✓ Extracted" -ForegroundColor Green
Write-Host ""

# Run installer
Write-Host "Configuring Quill..." -ForegroundColor Yellow
Push-Location $InstallDir

try {
    & powershell -NoProfile -ExecutionPolicy Bypass -File ".\install.ps1"
} catch {
    Write-Host "⚠ Configuration had issues, but core files are installed" -ForegroundColor Yellow
}

Pop-Location

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Installation Complete! 🎉" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Try it now:" -ForegroundColor Yellow
Write-Host "  cd $InstallDir" -ForegroundColor White
Write-Host "  .\quill.bat examples\example_simple.quill" -ForegroundColor White
Write-Host ""
Write-Host "Or just run:" -ForegroundColor Yellow
Write-Host "  python $InstallDir\core\quill.py $InstallDir\examples\example_simple.quill" -ForegroundColor White
Write-Host ""
Write-Host "Documentation: $InstallDir\README.md" -ForegroundColor Cyan
Write-Host ""
