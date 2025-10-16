# Icon Diagnostic Script
# Checks why icons might not be showing

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Icon Diagnostic Tool" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$iconPath = "$env:LOCALAPPDATA\StoryScript\storyscript_icon.ico"
$installPath = "$env:LOCALAPPDATA\StoryScript"

Write-Host "Checking installation..." -ForegroundColor Yellow
Write-Host ""

# Check 1: Icon file exists
Write-Host "[1] Icon file check:" -ForegroundColor Green
if (Test-Path $iconPath) {
    Write-Host "    ✓ Icon file exists: $iconPath" -ForegroundColor White
    $iconSize = (Get-Item $iconPath).Length
    Write-Host "    ✓ File size: $iconSize bytes" -ForegroundColor White
} else {
    Write-Host "    ✗ Icon file NOT found!" -ForegroundColor Red
    Write-Host "    Expected: $iconPath" -ForegroundColor Red
}

Write-Host ""

# Check 2: Registry keys
Write-Host "[2] Registry check:" -ForegroundColor Green

$ext = Get-ItemProperty -Path "HKCU:\Software\Classes\.story" -ErrorAction SilentlyContinue
if ($ext) {
    Write-Host "    ✓ .story extension registered" -ForegroundColor White
    Write-Host "      Points to: $($ext.'(default)')" -ForegroundColor Gray
} else {
    Write-Host "    ✗ .story extension NOT registered" -ForegroundColor Red
}

$fileType = Get-ItemProperty -Path "HKCU:\Software\Classes\StoryScript.File" -ErrorAction SilentlyContinue
if ($fileType) {
    Write-Host "    ✓ StoryScript.File type registered" -ForegroundColor White
} else {
    Write-Host "    ✗ StoryScript.File type NOT registered" -ForegroundColor Red
}

$icon = Get-ItemProperty -Path "HKCU:\Software\Classes\StoryScript.File\DefaultIcon" -ErrorAction SilentlyContinue
if ($icon) {
    Write-Host "    ✓ Icon registered in registry" -ForegroundColor White
    Write-Host "      Path: $($icon.'(default)')" -ForegroundColor Gray
} else {
    Write-Host "    ✗ Icon NOT registered" -ForegroundColor Red
}

Write-Host ""

# Check 3: File association
Write-Host "[3] File association check:" -ForegroundColor Green
$assoc = cmd /c assoc .story 2>$null
if ($assoc) {
    Write-Host "    ✓ Association: $assoc" -ForegroundColor White
} else {
    Write-Host "    ⚠ No association found" -ForegroundColor Yellow
}

$ftype = cmd /c ftype StoryScript.File 2>$null
if ($ftype) {
    Write-Host "    ✓ File type: $ftype" -ForegroundColor White
} else {
    Write-Host "    ⚠ No file type command" -ForegroundColor Yellow
}

Write-Host ""

# Check 4: Test .story file
Write-Host "[4] Test file check:" -ForegroundColor Green
$testFiles = Get-ChildItem -Path $PSScriptRoot -Filter "*.story" | Select-Object -First 3
if ($testFiles) {
    Write-Host "    Found .story files:" -ForegroundColor White
    foreach ($file in $testFiles) {
        Write-Host "      - $($file.Name)" -ForegroundColor Gray
    }
} else {
    Write-Host "    ⚠ No .story files found in current directory" -ForegroundColor Yellow
}

Write-Host ""

# Check 5: Icon cache
Write-Host "[5] Icon cache check:" -ForegroundColor Green
$cacheFiles = @(
    "$env:LOCALAPPDATA\IconCache.db",
    "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\iconcache_*.db"
)

$foundCache = $false
foreach ($cache in $cacheFiles) {
    if (Test-Path $cache) {
        Write-Host "    Found: $cache" -ForegroundColor Gray
        $foundCache = $true
    }
}

if ($foundCache) {
    Write-Host "    ⚠ Icon cache files exist (may need clearing)" -ForegroundColor Yellow
} else {
    Write-Host "    ✓ No old icon cache" -ForegroundColor White
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Diagnosis Complete" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Recommendations
Write-Host "Recommendations:" -ForegroundColor Yellow
Write-Host ""

if (Test-Path $iconPath) {
    Write-Host "✓ Installation looks good!" -ForegroundColor Green
    Write-Host ""
    Write-Host "To fix icon display, try:" -ForegroundColor Yellow
    Write-Host "  1. Run: .\fix_icon.bat" -ForegroundColor White
    Write-Host "  2. Or run: .\force_icon_refresh.ps1" -ForegroundColor White  
    Write-Host "  3. Or restart your computer" -ForegroundColor White
    Write-Host ""
    Write-Host "Note: Windows can be stubborn with icons!" -ForegroundColor Gray
    Write-Host "      Sometimes a full restart is the only way." -ForegroundColor Gray
} else {
    Write-Host "✗ Installation problem detected!" -ForegroundColor Red
    Write-Host ""
    Write-Host "To fix:" -ForegroundColor Yellow
    Write-Host "  1. Run: .\INSTALL_STORYSCRIPT_USER.bat" -ForegroundColor White
    Write-Host "  2. Make sure the install completes successfully" -ForegroundColor White
}

Write-Host ""
