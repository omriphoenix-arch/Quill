# Quill VS Code Extension Installer

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Quill VS Code Extension" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get paths
$extensionDir = "$env:USERPROFILE\.vscode\extensions\quill.quill-1.2.1"
$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Extension will be installed to:" -ForegroundColor Yellow
Write-Host "  $extensionDir" -ForegroundColor White
Write-Host ""

# Check if VS Code is running
$vscodeProcess = Get-Process -Name "Code" -ErrorAction SilentlyContinue
if ($vscodeProcess) {
    Write-Host "WARNING: VS Code is currently running!" -ForegroundColor Yellow
    Write-Host "Please close all VS Code windows before installing." -ForegroundColor Yellow
    Write-Host ""
    $response = Read-Host "Continue anyway? (y/n)"
    if ($response -ne "y") {
        Write-Host "Installation cancelled." -ForegroundColor Gray
        exit 0
    }
}

# Remove old version
if (Test-Path $extensionDir) {
    Write-Host "[1/4] Removing old version..." -ForegroundColor Green
    Remove-Item -Path $extensionDir -Recurse -Force
    Write-Host "  Old version removed" -ForegroundColor Gray
} else {
    Write-Host "[1/4] No previous version found" -ForegroundColor Green
}

# Create directory
Write-Host "[2/4] Creating extension directory..." -ForegroundColor Green
New-Item -ItemType Directory -Path $extensionDir -Force | Out-Null
Write-Host "  Directory created" -ForegroundColor Gray

# Copy files
Write-Host "[3/4] Copying extension files..." -ForegroundColor Green

# Copy main files
Copy-Item -Path "$sourceDir\package.json" -Destination $extensionDir
Copy-Item -Path "$sourceDir\language-configuration.json" -Destination $extensionDir
Copy-Item -Path "$sourceDir\README.md" -Destination $extensionDir

# Copy directories
Copy-Item -Path "$sourceDir\syntaxes" -Destination $extensionDir -Recurse
Copy-Item -Path "$sourceDir\icons" -Destination $extensionDir -Recurse
Copy-Item -Path "$sourceDir\themes" -Destination $extensionDir -Recurse

Write-Host "  All files copied" -ForegroundColor Gray

# Verify installation
Write-Host "[4/4] Verifying installation..." -ForegroundColor Green
$packageJson = Get-Content "$extensionDir\package.json" -Raw | ConvertFrom-Json
Write-Host "  Extension: $($packageJson.displayName)" -ForegroundColor Gray
Write-Host "  Version: $($packageJson.version)" -ForegroundColor Gray

# Check for icon
if (Test-Path "$extensionDir\icons\quill-icon.png") {
    Write-Host "  Icon: Found (PNG)" -ForegroundColor Gray
} elseif (Test-Path "$extensionDir\icons\quill-icon.svg") {
    Write-Host "  Icon: Found (SVG)" -ForegroundColor Gray
} else {
    Write-Host "  Icon: Missing!" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "To see your new icons:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Close ALL VS Code windows" -ForegroundColor White
Write-Host "   (Very important!)" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Reopen VS Code" -ForegroundColor White
Write-Host ""
Write-Host "3. Open a folder with .quill files" -ForegroundColor White
Write-Host "   Example: $sourceDir\..\games" -ForegroundColor Gray
Write-Host ""
Write-Host "4. (Optional) Enable icon theme:" -ForegroundColor White
Write-Host "   • Press Ctrl+Shift+P" -ForegroundColor Gray
Write-Host "   • Type: 'File Icon Theme'" -ForegroundColor Gray
Write-Host "   • Select: 'Quill File Icons'" -ForegroundColor Gray
Write-Host ""
Write-Host "Your .quill files will have beautiful icons! 🎨" -ForegroundColor Cyan
Write-Host ""

Read-Host "Press Enter to finish"
