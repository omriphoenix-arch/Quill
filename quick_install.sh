#!/bin/bash
# Quill One-Line Installer for Mac/Linux
# Usage: curl -sSL https://raw.githubusercontent.com/omriphoenix-arch/Quill/main/quick_install.sh | bash
# Or: bash quick_install.sh

INSTALL_DIR="$HOME/quill"
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
GRAY='\033[0;90m'
NC='\033[0m'

echo ""
echo -e "${CYAN}========================================"
echo "  Quill Quick Installer v1.0"
echo "========================================${NC}"
echo ""

# Check Python
echo -e "${YELLOW}Checking for Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)' 2>/dev/null)
    PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)' 2>/dev/null)
    
    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
        echo -e "${RED}✗ Python 3.8+ required (found $PYTHON_VERSION)${NC}"
        echo -e "${YELLOW}  Download: https://www.python.org/downloads/${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✓ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3.8+ required${NC}"
    echo -e "${YELLOW}  Download: https://www.python.org/downloads/${NC}"
    exit 1
fi

echo ""

# Download
echo -e "${YELLOW}Downloading Quill (0.77 MB)...${NC}"
TEMP_ZIP="/tmp/quill-main.zip"
URL="https://github.com/omriphoenix-arch/Quill/archive/refs/heads/main.zip"

if curl -sSL "$URL" -o "$TEMP_ZIP"; then
    echo -e "${GREEN}✓ Downloaded${NC}"
else
    echo -e "${RED}✗ Download failed${NC}"
    echo -e "${YELLOW}  Please check your internet connection${NC}"
    exit 1
fi

echo ""

# Extract
echo -e "${YELLOW}Installing to $INSTALL_DIR...${NC}"
if [ -d "$INSTALL_DIR" ]; then
    echo -e "${GRAY}  Removing previous installation...${NC}"
    rm -rf "$INSTALL_DIR"
fi

mkdir -p "$INSTALL_DIR"

if command -v unzip &> /dev/null; then
    unzip -q "$TEMP_ZIP" -d "$INSTALL_DIR"
else
    echo -e "${YELLOW}⚠ unzip not found, using tar...${NC}"
    tar -xzf "$TEMP_ZIP" -C "$INSTALL_DIR"
fi

# Move contents up one level
EXTRACTED_DIR=$(find "$INSTALL_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)
if [ -n "$EXTRACTED_DIR" ]; then
    mv "$EXTRACTED_DIR"/* "$INSTALL_DIR/" 2>/dev/null
    mv "$EXTRACTED_DIR"/.[!.]* "$INSTALL_DIR/" 2>/dev/null
    rmdir "$EXTRACTED_DIR" 2>/dev/null
fi

rm "$TEMP_ZIP"
echo -e "${GREEN}✓ Extracted${NC}"
echo ""

# Run installer
echo -e "${YELLOW}Configuring Quill...${NC}"
cd "$INSTALL_DIR"

if [ -f "install.sh" ]; then
    chmod +x install.sh
    bash install.sh
else
    echo -e "${YELLOW}⚠ Installer not found, but core files are installed${NC}"
fi

echo ""
echo -e "${GREEN}========================================"
echo "  Installation Complete! 🎉"
echo "========================================${NC}"
echo ""
echo -e "${YELLOW}Try it now:${NC}"
echo -e "  ${NC}cd $INSTALL_DIR${NC}"
echo -e "  ${NC}./quill examples/example_simple.quill${NC}"
echo ""
echo -e "${YELLOW}Or just run:${NC}"
echo -e "  ${NC}python3 $INSTALL_DIR/core/quill.py $INSTALL_DIR/examples/example_simple.quill${NC}"
echo ""
echo -e "${CYAN}Documentation: $INSTALL_DIR/README.md${NC}"
echo ""
