# StoryScript Installer for Windows
# This script installs StoryScript as a system-wide application

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   StoryScript Language Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the source directory (where this script is)
$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Installation directory
$installDir = "$env:ProgramFiles\StoryScript"

Write-Host "Installing StoryScript to: $installDir" -ForegroundColor Yellow
Write-Host ""

# Check for admin rights
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This installer requires administrator privileges!" -ForegroundColor Red
    Write-Host "Right-click PowerShell and select 'Run as Administrator', then try again." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Create installation directory
Write-Host "[1/5] Creating installation directory..." -ForegroundColor Green
if (Test-Path $installDir) {
    Remove-Item -Path $installDir -Recurse -Force
}
New-Item -ItemType Directory -Path $installDir -Force | Out-Null

# Copy core files
Write-Host "[2/5] Copying StoryScript files..." -ForegroundColor Green
Copy-Item -Path "$sourceDir\storyscript.py" -Destination $installDir
Copy-Item -Path "$sourceDir\lexer.py" -Destination $installDir
Copy-Item -Path "$sourceDir\parser.py" -Destination $installDir
Copy-Item -Path "$sourceDir\interpreter.py" -Destination $installDir
Copy-Item -Path "$sourceDir\storyscript.bat" -Destination $installDir
Copy-Item -Path "$sourceDir\README.md" -Destination $installDir

# Copy icon file if it exists
if (Test-Path "$sourceDir\storyscript_icon.ico") {
    Copy-Item -Path "$sourceDir\storyscript_icon.ico" -Destination $installDir
    Write-Host "    Icon file copied!" -ForegroundColor Gray
}

# Copy examples and docs
if (Test-Path "$sourceDir\examples") {
    Copy-Item -Path "$sourceDir\examples" -Destination $installDir -Recurse
}
if (Test-Path "$sourceDir\docs") {
    Copy-Item -Path "$sourceDir\docs" -Destination $installDir -Recurse
}

# Add to PATH
Write-Host "[3/5] Adding StoryScript to system PATH..." -ForegroundColor Green
$currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
if ($currentPath -notlike "*$installDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$installDir", "Machine")
    Write-Host "    Added to PATH successfully!" -ForegroundColor Gray
} else {
    Write-Host "    Already in PATH" -ForegroundColor Gray
}

# Create Start Menu shortcut
Write-Host "[4/5] Creating Start Menu shortcuts..." -ForegroundColor Green
$startMenuDir = "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\StoryScript"
New-Item -ItemType Directory -Path $startMenuDir -Force | Out-Null

# Create shortcut to documentation
$shell = New-Object -ComObject WScript.Shell
$docsShortcut = $shell.CreateShortcut("$startMenuDir\StoryScript Documentation.lnk")
$docsShortcut.TargetPath = "$installDir\README.md"
$docsShortcut.Save()

# Create shortcut to examples folder
$examplesShortcut = $shell.CreateShortcut("$startMenuDir\StoryScript Examples.lnk")
$examplesShortcut.TargetPath = "$installDir\examples"
$examplesShortcut.Save()

# Create file association
Write-Host "[5/5] Setting up .story file association..." -ForegroundColor Green
$storyCommand = "python `"$installDir\storyscript.py`" `"%1`""

# Register .story extension
New-Item -Path "HKCR:\.story" -Force | Out-Null
Set-ItemProperty -Path "HKCR:\.story" -Name "(Default)" -Value "StoryScript.File"

# Create file type
New-Item -Path "HKCR:\StoryScript.File" -Force | Out-Null
Set-ItemProperty -Path "HKCR:\StoryScript.File" -Name "(Default)" -Value "StoryScript Program"

# Create icon (use custom icon if available, fallback to Python icon)
New-Item -Path "HKCR:\StoryScript.File\DefaultIcon" -Force | Out-Null
if (Test-Path "$installDir\storyscript_icon.ico") {
    Set-ItemProperty -Path "HKCR:\StoryScript.File\DefaultIcon" -Name "(Default)" -Value "$installDir\storyscript_icon.ico,0"
    Write-Host "    Custom icon assigned to .story files!" -ForegroundColor Gray
} else {
    Set-ItemProperty -Path "HKCR:\StoryScript.File\DefaultIcon" -Name "(Default)" -Value "python.exe,0"
    Write-Host "    Using default icon for .story files" -ForegroundColor Gray
}

# Create open command
New-Item -Path "HKCR:\StoryScript.File\shell\open\command" -Force | Out-Null
Set-ItemProperty -Path "HKCR:\StoryScript.File\shell\open\command" -Name "(Default)" -Value $storyCommand

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "StoryScript is now installed!" -ForegroundColor Cyan
Write-Host ""
Write-Host "You can now:" -ForegroundColor Yellow
Write-Host "  • Type 'storyscript' in any command prompt" -ForegroundColor White
Write-Host "  • Double-click .story files to run them" -ForegroundColor White
Write-Host "  • Find StoryScript in your Start Menu" -ForegroundColor White
Write-Host ""
Write-Host "Try it out:" -ForegroundColor Yellow
Write-Host "  storyscript $installDir\examples\tutorial.story" -ForegroundColor Cyan
Write-Host ""
Write-Host "NOTE: Close and reopen any command prompts for PATH to take effect" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to finish"
