# StoryScript Icon Applicator
# Applies the current icon to .story file associations

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   StoryScript Icon Refresh" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$iconPath = Join-Path $scriptDir "storyscript_icon.ico"

Write-Host "Icon location: " -NoNewline
Write-Host $iconPath -ForegroundColor Yellow
Write-Host ""

# Check if icon exists
if (-not (Test-Path $iconPath)) {
    Write-Host "ERROR: Icon file not found!" -ForegroundColor Red
    Write-Host "Expected: $iconPath" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Please make sure storyscript_icon.ico exists in the icons folder." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[1/5] Checking current icon..." -ForegroundColor Green
$currentIconPath = (Get-ItemProperty -Path "HKCU:\Software\Classes\StoryScript.File\DefaultIcon" -ErrorAction SilentlyContinue).'(Default)'
if ($currentIconPath) {
    Write-Host "  Current: $currentIconPath" -ForegroundColor Gray
} else {
    Write-Host "  No icon currently set" -ForegroundColor Gray
}
Write-Host ""

Write-Host "[2/5] Updating registry..." -ForegroundColor Green

# Register .story extension
New-Item -Path "HKCU:\Software\Classes\.story" -Force | Out-Null
Set-ItemProperty -Path "HKCU:\Software\Classes\.story" -Name "(Default)" -Value "StoryScript.File"
Write-Host "  .story extension registered" -ForegroundColor Gray

# Create file type
New-Item -Path "HKCU:\Software\Classes\StoryScript.File" -Force | Out-Null
Set-ItemProperty -Path "HKCU:\Software\Classes\StoryScript.File" -Name "(Default)" -Value "StoryScript Program"
Write-Host "  File type created" -ForegroundColor Gray

# Set icon
New-Item -Path "HKCU:\Software\Classes\StoryScript.File\DefaultIcon" -Force | Out-Null
Set-ItemProperty -Path "HKCU:\Software\Classes\StoryScript.File\DefaultIcon" -Name "(Default)" -Value "$iconPath,0"
Write-Host "  Icon path updated" -ForegroundColor Gray

# Set open command (if Python is available)
$pythonPath = (Get-Command python -ErrorAction SilentlyContinue).Source
if ($pythonPath) {
    $storyscriptPath = Join-Path (Split-Path -Parent (Split-Path -Parent $scriptDir)) "core\storyscript.py"
    if (Test-Path $storyscriptPath) {
        $openCommand = "python `"$storyscriptPath`" `"%1`""
        New-Item -Path "HKCU:\Software\Classes\StoryScript.File\shell\open\command" -Force | Out-Null
        Set-ItemProperty -Path "HKCU:\Software\Classes\StoryScript.File\shell\open\command" -Name "(Default)" -Value $openCommand
        Write-Host "  Open command configured" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "[3/5] Clearing icon cache..." -ForegroundColor Green
try {
    & ie4uinit.exe -show 2>$null
    Write-Host "  Icon cache cleared" -ForegroundColor Gray
} catch {
    Write-Host "  Warning: Could not clear icon cache" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[4/5] Notifying Windows of changes..." -ForegroundColor Green

# Notify Windows shell of changes
$signature = @'
[DllImport("shell32.dll", CharSet = CharSet.Auto, SetLastError = true)]
public static extern void SHChangeNotify(uint wEventId, uint uFlags, IntPtr dwItem1, IntPtr dwItem2);
'@

Add-Type -MemberDefinition $signature -Name ShellNotify -Namespace Win32

# SHCNE_ASSOCCHANGED = 0x08000000, SHCNF_IDLIST = 0x0000
[Win32.ShellNotify]::SHChangeNotify(0x08000000, 0x0000, [IntPtr]::Zero, [IntPtr]::Zero)
Write-Host "  Shell notified of association changes" -ForegroundColor Gray

Write-Host ""
Write-Host "[5/5] Restarting Windows Explorer..." -ForegroundColor Green

# Ask user if they want to restart Explorer
Write-Host ""
Write-Host "Windows Explorer needs to restart to see the new icon." -ForegroundColor Yellow
$response = Read-Host "Restart Explorer now? (Y/n)"

if ($response -eq "" -or $response -eq "y" -or $response -eq "Y") {
    Write-Host "  Stopping Explorer..." -ForegroundColor Gray
    Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
    Write-Host "  Starting Explorer..." -ForegroundColor Gray
    Start-Process explorer.exe
    Write-Host "  Explorer restarted!" -ForegroundColor Gray
} else {
    Write-Host "  Skipped - you'll need to restart Explorer manually or reboot" -ForegroundColor Gray
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Icon Refresh Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your .story files should now display:" -ForegroundColor Cyan
Write-Host "  $(Split-Path -Leaf $iconPath)" -ForegroundColor White
Write-Host ""
Write-Host "If you don't see the icon immediately:" -ForegroundColor Yellow
Write-Host "  1. Navigate to a folder with .story files" -ForegroundColor White
Write-Host "  2. Press F5 to refresh" -ForegroundColor White
Write-Host "  3. Try viewing as Large/Medium icons" -ForegroundColor White
Write-Host "  4. Restart your computer if needed" -ForegroundColor White
Write-Host ""

# Show which icon is active
$iconInfo = Get-Item $iconPath
Write-Host "Active icon details:" -ForegroundColor Cyan
Write-Host "  File: $($iconInfo.Name)" -ForegroundColor White
Write-Host "  Size: $([math]::Round($iconInfo.Length / 1KB, 2)) KB" -ForegroundColor White
Write-Host "  Modified: $($iconInfo.LastWriteTime)" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to finish"
