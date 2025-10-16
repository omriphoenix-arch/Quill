# Bulk Rebrand Script: StoryScript -> Quill
# This script updates all text files in the project

$rootPath = "C:\Users\Omri.Morgan02\Downloads\possible"

Write-Host "Starting Quill rebrand..." -ForegroundColor Cyan
Write-Host "This will update all documentation and code files." -ForegroundColor Yellow
Write-Host ""

# Define replacements
$replacements = @{
    "StoryScript" = "Quill"
    "storyscript" = "quill"
    "STORYSCRIPT" = "QUILL"
    "\.story" = ".quill"
    "story files" = "quill files"
    "Story files" = "Quill files"
    ".story extension" = ".quill extension"
    "storyscript.py" = "quill.py"
    "storyscript.bat" = "quill.bat"
}

# File types to process
$extensions = @("*.md", "*.py", "*.ps1", "*.sh", "*.bat", "*.json", "*.txt", "*.quill")

$filesProcessed = 0
$replacementsMade = 0

foreach ($ext in $extensions) {
    $files = Get-ChildItem -Path $rootPath -Filter $ext -Recurse -File -ErrorAction SilentlyContinue
    
    foreach ($file in $files) {
        # Skip certain directories/files
        if ($file.FullName -match "\.git|node_modules|__pycache__|\.ico|\.png|\.svg") {
            continue
        }
        
        try {
            $content = Get-Content $file.FullName -Raw -ErrorAction Stop
            $originalContent = $content
            
            # Apply all replacements
            foreach ($key in $replacements.Keys) {
                $value = $replacements[$key]
                if ($content -match $key) {
                    $content = $content -replace $key, $value
                }
            }
            
            # Only write if changed
            if ($content -ne $originalContent) {
                Set-Content -Path $file.FullName -Value $content -NoNewline
                $filesProcessed++
                Write-Host "✓ Updated: $($file.Name)" -ForegroundColor Green
            }
        }
        catch {
            Write-Host "✗ Error processing: $($file.Name)" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Rebrand Complete!" -ForegroundColor Green
Write-Host "Files updated: $filesProcessed" -ForegroundColor Yellow
Write-Host "════════════════════════════════════════" -ForegroundColor Cyan
