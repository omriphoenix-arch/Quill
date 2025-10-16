# Force Icon Refresh - Aggressive Method

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Force Icon Refresh" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Step 1: Clearing icon cache files..." -ForegroundColor Yellow

# Delete all icon cache files
$iconCaches = @(
    "$env:LOCALAPPDATA\IconCache.db",
    "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\iconcache_*.db",
    "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\thumbcache_*.db"
)

foreach ($cache in $iconCaches) {
    if (Test-Path $cache) {
        Remove-Item $cache -Force -ErrorAction SilentlyContinue
        Write-Host "  Deleted: $cache" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "Step 2: Notifying Windows of changes..." -ForegroundColor Yellow

# Notify shell of association change
$code = @"
using System;
using System.Runtime.InteropServices;

public class Shell32 {
    [DllImport("shell32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    public static extern void SHChangeNotify(uint wEventId, uint uFlags, IntPtr dwItem1, IntPtr dwItem2);
}
"@

Add-Type -TypeDefinition $code -ErrorAction SilentlyContinue
[Shell32]::SHChangeNotify(0x08000000, 0x0000, [IntPtr]::Zero, [IntPtr]::Zero)

Write-Host "  Shell notified of changes" -ForegroundColor Gray

Write-Host ""
Write-Host "Step 3: Refreshing icon cache..." -ForegroundColor Yellow
ie4uinit.exe -show
Write-Host "  Icon cache refreshed" -ForegroundColor Gray

Write-Host ""
Write-Host "Step 4: Restarting Windows Explorer..." -ForegroundColor Yellow
Stop-Process -Name explorer -Force
Write-Host "  Explorer restarted" -ForegroundColor Gray

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Refresh Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Now check your .story files in File Explorer!" -ForegroundColor Cyan
Write-Host ""
Write-Host "If icons still don't show:" -ForegroundColor Yellow
Write-Host "  1. Try restarting your computer" -ForegroundColor White
Write-Host "  2. Or right-click a .story file and check 'Opens with'" -ForegroundColor White
Write-Host ""
