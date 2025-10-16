# Unregister .quill file association and remove project from user PATH

param(
    [string] $QuillPath = "c:\Users\Omri.Morgan02\Downloads\possible"
)

$extension = ".quill"
$progId = "QuillFile"

Write-Host "Unregistering $extension file association (user scope)..." -ForegroundColor Yellow

# Remove file association from HKCU
$hkcu = 'HKCU:\Software\Classes'
$extKey = Join-Path $hkcu ("$extension")
$progKey = Join-Path $hkcu ("$progId")

if (Test-Path $extKey) {
    Remove-Item -Path $extKey -Recurse -Force
    Write-Host "Removed file extension registration: $extension"
}

if (Test-Path $progKey) {
    Remove-Item -Path $progKey -Recurse -Force
    Write-Host "Removed program ID: $progId"
}

# Remove project folder from user PATH
$envPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
if ($envPath -like "*${QuillPath}*") {
    Write-Host "Removing $QuillPath from user PATH..."
    $newPath = ($envPath -split ';' | Where-Object { $_ -ne $QuillPath }) -join ';'
    [Environment]::SetEnvironmentVariable('PATH', $newPath, 'User')
    Write-Host "Removed from PATH. Start a new shell for changes to take effect."
} else {
    Write-Host "Project path not found in user PATH."
}

Write-Host "`nUnregistration complete!" -ForegroundColor Green
Write-Host "You may need to restart VS Code or File Explorer for changes to take full effect."
