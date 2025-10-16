# Register .quill file association and add project quill launcher to user PATH
# Run this script in an elevated PowerShell if you want to make system-wide changes.

param(
    [string] $QuillPath = "c:\Users\Omri.Morgan02\Downloads\possible",
    [switch] $Force
)

$extension = ".quill"
$progId = "QuillFile"
$description = "Quill Story Files"
$launcherName = "quill.bat"
$launcherPath = Join-Path $QuillPath $launcherName

Write-Host "Registering $extension files to open with $launcherPath (user scope)..."

# Ensure launcher exists
if (-not (Test-Path $launcherPath)) {
    Write-Host "Launcher not found at $launcherPath" -ForegroundColor Yellow
    Write-Host "Looking for core/quill.py to create a temporary launcher..."
    $quillPy = Join-Path $QuillPath "core\quill.py"
    if (Test-Path $quillPy) {
        # Use PowerShell's backtick to escape embedded quotes so the variable expands correctly
        $batContent = "@echo off`npython `"$quillPy`" %*"
        New-Item -Path $launcherPath -ItemType File -Force -Value $batContent | Out-Null
        Write-Host "Created launcher at $launcherPath"
    } else {
        Write-Host "core/quill.py not found at $quillPy. Aborting." -ForegroundColor Red
        exit 1
    }
}

# Create file association under HKCU (current user)
$hkcu = 'HKCU:\Software\Classes'
$extKey = Join-Path $hkcu ("$extension")
New-Item -Path $extKey -Force | Out-Null
Set-ItemProperty -Path $extKey -Name '(Default)' -Value $progId

$progKey = Join-Path $hkcu ("$progId")
New-Item -Path $progKey -Force | Out-Null
Set-ItemProperty -Path $progKey -Name '(Default)' -Value $description

# Set command to open with launcher
$commandKey = Join-Path $progKey 'shell\open\command'
$command = '"' + $launcherPath + '" "%1" %*'
New-Item -Path $commandKey -Force | Out-Null
Set-ItemProperty -Path $commandKey -Name '(Default)' -Value $command

Write-Host "File association created: $extension -> $launcherPath"

# Add project folder to user PATH if not present
$envPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
if ($envPath -notlike "*${QuillPath}*" -or $Force) {
    Write-Host "Adding $QuillPath to user PATH..."
    [Environment]::SetEnvironmentVariable('PATH', "$envPath;$QuillPath", 'User')
    Write-Host "Added. You may need to start a new shell for PATH changes to take effect."
} else {
    Write-Host "Project path already in user PATH."
}

Write-Host "Done. To test right away in this session, run: & \"$launcherPath\" examples\example_simple.quill"
