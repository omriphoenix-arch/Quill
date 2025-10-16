# Quill v1.0.1 Testing Script
# Tests all example files for basic execution

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Quill v1.0.1 Example Testing Suite" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$exampleFiles = @(
    "examples/example_simple.quill",
    "examples/example_adventure.quill",
    "examples/example_calculator.quill",
    "examples/example_guessing_game.quill",
    "examples/example_mystery.quill",
    "examples/demo_inventory.quill",
    "examples/demo_randomizer.quill",
    "examples/demo_saveload.quill",
    "examples/demo_wait.quill"
)

$passed = 0
$failed = 0
$results = @()

foreach ($file in $exampleFiles) {
    Write-Host "Testing: $file" -ForegroundColor Yellow
    
    # Test if file exists
    if (-not (Test-Path $file)) {
        Write-Host "  ✗ File not found!" -ForegroundColor Red
        $failed++
        $results += [PSCustomObject]@{
            File = $file
            Status = "MISSING"
            Error = "File not found"
        }
        continue
    }
    
    # Try to run the file (timeout after 3 seconds for interactive programs)
    try {
        # Use Start-Process with timeout for interactive programs
        $process = Start-Process -FilePath "python" `
                                 -ArgumentList "core/quill.py", $file `
                                 -NoNewWindow `
                                 -PassThru `
                                 -RedirectStandardOutput "temp_output.txt" `
                                 -RedirectStandardError "temp_error.txt" `
                                 -RedirectStandardInput "temp_input.txt"
        
        # Wait max 3 seconds
        $timeout = $process | Wait-Process -Timeout 3 -ErrorAction SilentlyContinue
        
        if (-not $process.HasExited) {
            # Kill if still running (interactive program)
            $process | Stop-Process -Force
            Write-Host "  ⚠ Interactive program (killed after 3s)" -ForegroundColor Yellow
            $results += [PSCustomObject]@{
                File = $file
                Status = "INTERACTIVE"
                Error = "Requires user input"
            }
        } elseif ($process.ExitCode -eq 0) {
            Write-Host "  ✓ Passed" -ForegroundColor Green
            $passed++
            $results += [PSCustomObject]@{
                File = $file
                Status = "PASSED"
                Error = ""
            }
        } else {
            Write-Host "  ✗ Failed (Exit code: $($process.ExitCode))" -ForegroundColor Red
            $errorContent = Get-Content "temp_error.txt" -Raw
            $failed++
            $results += [PSCustomObject]@{
                File = $file
                Status = "FAILED"
                Error = $errorContent
            }
        }
    } catch {
        Write-Host "  ✗ Error: $_" -ForegroundColor Red
        $failed++
        $results += [PSCustomObject]@{
            File = $file
            Status = "ERROR"
            Error = $_.Exception.Message
        }
    }
    
    # Clean up temp files
    Remove-Item "temp_*.txt" -ErrorAction SilentlyContinue
    
    Write-Host ""
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Test Results Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total Tested: $($exampleFiles.Count)" -ForegroundColor White
Write-Host "Passed: $passed" -ForegroundColor Green
Write-Host "Failed: $failed" -ForegroundColor Red
Write-Host "Interactive: $(($results | Where-Object {$_.Status -eq 'INTERACTIVE'}).Count)" -ForegroundColor Yellow

# Detailed results
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Detailed Results" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$results | Format-Table -AutoSize

Write-Host "`nTest completed at $(Get-Date)" -ForegroundColor Gray
