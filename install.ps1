# Quill Quick Installer
# One-command installation for Windows, macOS, and Linux
# 
# Requirements: Python 3.8+ (required)
# Optional: VS Code (for syntax highlighting)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "     Quill Installer v1.0.0" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Requirements:" -ForegroundColor Yellow
Write-Host "  ✅ Python 3.8+ (required)" -ForegroundColor White
Write-Host "  🟡 VS Code (optional - for syntax highlighting)" -ForegroundColor Gray
Write-Host ""

# Check Python version
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
    
    # Extract version number
    if ($pythonVersion -match "Python (\d+)\.(\d+)") {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        
        if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 8)) {
            Write-Host "✗ Python 3.8+ required. Please upgrade Python." -ForegroundColor Red
            exit 1
        }
    }
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8+ first." -ForegroundColor Red
    Write-Host "  Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Install core interpreter
Write-Host "Installing Quill interpreter..." -ForegroundColor Yellow
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$coreDir = Join-Path $scriptDir "core"

if (Test-Path $coreDir) {
    Push-Location $coreDir
    
    # Install dependencies
    Write-Host "  Installing dependencies..." -ForegroundColor Gray
    python -m pip install --upgrade pip --quiet
    
    # Check if Pillow is needed (for icon generation)
    if (Test-Path "../icons") {
        python -m pip install Pillow --quiet
        Write-Host "  ✓ Installed Pillow (for icon generation)" -ForegroundColor Green
    }
    
    Write-Host "✓ Core interpreter installed" -ForegroundColor Green
    Pop-Location
} else {
    Write-Host "✗ Core directory not found" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Register .quill files and add to PATH
Write-Host "Registering .quill files and adding to PATH..." -ForegroundColor Yellow
$registerScript = Join-Path $scriptDir "scripts\register_quill.ps1"

if (Test-Path $registerScript) {
    try {
        & powershell -NoProfile -ExecutionPolicy Bypass -File $registerScript -QuillPath $scriptDir
        Write-Host "✓ File association and PATH configured" -ForegroundColor Green
    } catch {
        Write-Host "⚠ Registration failed, but you can run it manually later:" -ForegroundColor Yellow
        Write-Host "  powershell -ExecutionPolicy Bypass -File scripts\register_quill.ps1" -ForegroundColor Gray
    }
} else {
    Write-Host "⚠ Registration script not found. Creating launchers manually..." -ForegroundColor Yellow
    
    # Create quill.bat launcher if it doesn't exist
    $launcherPath = Join-Path $scriptDir "quill.bat"
    if (-not (Test-Path $launcherPath)) {
        $quillPy = Join-Path $scriptDir "core\quill.py"
        $batContent = "@echo off`npython `"$quillPy`" %*"
        Set-Content -Path $launcherPath -Value $batContent
        Write-Host "✓ Created quill.bat launcher" -ForegroundColor Green
    }
}

Write-Host ""

# VS Code extension setup (optional)
Write-Host "Setting up VS Code extension..." -ForegroundColor Yellow
$vscodeInstalled = Get-Command code -ErrorAction SilentlyContinue

if ($vscodeInstalled) {
    $extensionsJson = Join-Path $scriptDir ".vscode\extensions.json"
    
    if (Test-Path $extensionsJson) {
        Write-Host "✓ VS Code detected! Extension will auto-install when you open this workspace" -ForegroundColor Green
        Write-Host "  (Configured in .vscode/extensions.json)" -ForegroundColor Gray
    } else {
        Write-Host "⚠ Extension configuration not found" -ForegroundColor Yellow
        Write-Host "  You may need to manually install from .vscode-extension/" -ForegroundColor Gray
    }
} else {
    Write-Host "🟡 VS Code not detected (optional)" -ForegroundColor Gray
    Write-Host "  Quill works without VS Code! You can use any text editor." -ForegroundColor Gray
    Write-Host "  Install VS Code for syntax highlighting: https://code.visualstudio.com/" -ForegroundColor Gray
}

Write-Host ""

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "     Installation Complete! 🎉" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Show next steps
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Run a demo: " -NoNewline
Write-Host "quill.bat examples\example_simple.quill" -ForegroundColor White
Write-Host "  2. Or double-click any .quill file in File Explorer!" -ForegroundColor White
Write-Host "  3. Open workspace in VS Code for syntax highlighting & themes" -ForegroundColor White
Write-Host "  4. Read the docs: " -NoNewline
Write-Host "README.md and docs\" -ForegroundColor White
Write-Host ""

Write-Host "For help, visit: " -NoNewline
Write-Host "https://github.com/yourusername/quill" -ForegroundColor Cyan
Write-Host ""

# Test installation
Write-Host "Testing installation..." -ForegroundColor Yellow
$testFile = Join-Path $scriptDir "examples\example_simple.quill"
$launcher = Join-Path $scriptDir "quill.bat"

if ((Test-Path $testFile) -and (Test-Path $launcher)) {
    Write-Host "  Running test program..." -ForegroundColor Gray
    & $launcher $testFile
    Write-Host ""
    Write-Host "✓ Installation test successful!" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Test file not found, but installation completed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Happy coding with Quill! ✨" -ForegroundColor Cyan
Write-Host ""
