# StoryScript User Installation (No Admin Required!)
# Installs to your user folder instead of Program Files

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   StoryScript User Installer" -ForegroundColor Cyan
Write-Host "   (No Admin Required!)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the source directory
$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Install to user's local app data (no admin needed!)
$installDir = "$env:LOCALAPPDATA\StoryScript"

Write-Host "Installing StoryScript to: $installDir" -ForegroundColor Yellow
Write-Host "(This location doesn't require admin privileges)" -ForegroundColor Gray
Write-Host ""

# Create installation directory
Write-Host "[1/5] Creating installation directory..." -ForegroundColor Green
if (Test-Path $installDir) {
    Write-Host "    Removing old installation..." -ForegroundColor Gray
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
    Write-Host "    Examples copied!" -ForegroundColor Gray
}
if (Test-Path "$sourceDir\docs") {
    Copy-Item -Path "$sourceDir\docs" -Destination $installDir -Recurse
    Write-Host "    Documentation copied!" -ForegroundColor Gray
}

# Add to USER PATH (not system PATH - no admin needed!)
Write-Host "[3/5] Adding StoryScript to your PATH..." -ForegroundColor Green
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($currentPath -notlike "*$installDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$installDir", "User")
    Write-Host "    Added to your user PATH successfully!" -ForegroundColor Gray
    Write-Host "    (Only affects your account, not system-wide)" -ForegroundColor Gray
} else {
    Write-Host "    Already in PATH" -ForegroundColor Gray
}

# Create Start Menu shortcuts (user level)
Write-Host "[4/5] Creating Start Menu shortcuts..." -ForegroundColor Green
$startMenuDir = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\StoryScript"
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

Write-Host "    Start Menu shortcuts created (in your user account)" -ForegroundColor Gray

# Create file association (USER LEVEL - no admin needed!)
Write-Host "[5/5] Setting up .story file association..." -ForegroundColor Green

# User-level registry key (HKEY_CURRENT_USER instead of HKEY_CLASSES_ROOT)
$userClasses = "HKCU:\Software\Classes"

# Register .story extension
New-Item -Path "$userClasses\.story" -Force | Out-Null
Set-ItemProperty -Path "$userClasses\.story" -Name "(Default)" -Value "StoryScript.File"
Write-Host "    .story extension registered" -ForegroundColor Gray

# Create file type
New-Item -Path "$userClasses\StoryScript.File" -Force | Out-Null
Set-ItemProperty -Path "$userClasses\StoryScript.File" -Name "(Default)" -Value "StoryScript Program"

# Set custom icon (user level)
New-Item -Path "$userClasses\StoryScript.File\DefaultIcon" -Force | Out-Null
if (Test-Path "$installDir\storyscript_icon.ico") {
    Set-ItemProperty -Path "$userClasses\StoryScript.File\DefaultIcon" -Name "(Default)" -Value "$installDir\storyscript_icon.ico,0"
    Write-Host "    Custom icon assigned to .story files!" -ForegroundColor Gray
} else {
    # Fallback to Python icon
    Set-ItemProperty -Path "$userClasses\StoryScript.File\DefaultIcon" -Name "(Default)" -Value "python.exe,0"
    Write-Host "    Using Python icon for .story files" -ForegroundColor Gray
}

# Create open command
$storyCommand = "python `"$installDir\storyscript.py`" `"%1`""
New-Item -Path "$userClasses\StoryScript.File\shell\open\command" -Force | Out-Null
Set-ItemProperty -Path "$userClasses\StoryScript.File\shell\open\command" -Name "(Default)" -Value $storyCommand
Write-Host "    Double-click support enabled" -ForegroundColor Gray

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "StoryScript is now installed for YOUR USER ACCOUNT!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Installation Location:" -ForegroundColor Yellow
Write-Host "  $installDir" -ForegroundColor White
Write-Host ""
Write-Host "You can now:" -ForegroundColor Yellow
Write-Host "  • Type 'storyscript' in any command prompt" -ForegroundColor White
Write-Host "  • Double-click .story files to run them" -ForegroundColor White
Write-Host "  • Find StoryScript in your Start Menu" -ForegroundColor White
Write-Host ""
Write-Host "Try it out:" -ForegroundColor Yellow
Write-Host "  storyscript $installDir\examples\demo_wait.story" -ForegroundColor Cyan
Write-Host ""
Write-Host "IMPORTANT:" -ForegroundColor Yellow
Write-Host "  Close and reopen any command prompts for PATH to take effect" -ForegroundColor White
Write-Host ""
Write-Host "To see the icon:" -ForegroundColor Yellow
Write-Host "  1. Close this PowerShell window" -ForegroundColor White
Write-Host "  2. Open File Explorer" -ForegroundColor White
Write-Host "  3. Navigate to your .story files" -ForegroundColor White
Write-Host "  4. You should see the custom icon!" -ForegroundColor White
Write-Host ""
Write-Host "If icon doesn't show, run:" -ForegroundColor Yellow
Write-Host "  ie4uinit.exe -show" -ForegroundColor Cyan
Write-Host ""
Write-Host "NOTE: This installation only affects YOUR account." -ForegroundColor Gray
Write-Host "      Other users on this computer won't see StoryScript." -ForegroundColor Gray
Write-Host ""
Read-Host "Press Enter to finish"
