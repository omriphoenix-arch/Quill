#!/bin/bash
# Quill Installer for macOS and Linux
# Quick installation script
#
# Requirements: Python 3.8+ (required)
# Optional: VS Code (for syntax highlighting)

echo ""
echo "========================================"
echo "   Quill Installer v1.0.0"
echo "========================================"
echo ""
echo "Requirements:"
echo "  ✅ Python 3.8+ (required)"
echo "  🟡 VS Code (optional - for syntax highlighting)"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${YELLOW}Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Found: $PYTHON_VERSION${NC}"
    
    # Check if version is 3.8+
    PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
    PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
    
    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
        echo -e "${RED}✗ Python 3.8+ required. Please upgrade Python.${NC}"
        exit 1
    fi
else
    echo -e "${RED}✗ Python not found. Please install Python 3.8+ first.${NC}"
    echo -e "${YELLOW}  Download from: https://www.python.org/downloads/${NC}"
    exit 1
fi

echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Install core interpreter
echo -e "${YELLOW}Installing Quill interpreter...${NC}"
CORE_DIR="$SCRIPT_DIR/core"

if [ -d "$CORE_DIR" ]; then
    cd "$CORE_DIR"
    
    # Install dependencies
    echo -e "  ${YELLOW}Installing dependencies...${NC}"
    python3 -m pip install --upgrade pip --quiet
    
    # Check if Pillow is needed
    if [ -d "$SCRIPT_DIR/icons" ]; then
        python3 -m pip install Pillow --quiet
        echo -e "  ${GREEN}✓ Installed Pillow (for icon generation)${NC}"
    fi
    
    echo -e "${GREEN}✓ Core interpreter installed${NC}"
    cd "$SCRIPT_DIR"
else
    echo -e "${RED}✗ Core directory not found${NC}"
    exit 1
fi

echo ""

# Create and configure launcher
echo -e "${YELLOW}Setting up quill launcher...${NC}"
LAUNCHER="$SCRIPT_DIR/quill"

if [ ! -f "$LAUNCHER" ]; then
    cat > "$LAUNCHER" << 'EOF'
#!/bin/bash
# Quill launcher script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 "$SCRIPT_DIR/core/quill.py" "$@"
EOF
    chmod +x "$LAUNCHER"
    echo -e "${GREEN}✓ Created quill launcher${NC}"
else
    echo -e "${GREEN}✓ Launcher already exists${NC}"
fi

# Add to PATH
echo -e "${YELLOW}Would you like to add Quill to your PATH? (y/n): ${NC}"
read -r ADD_PATH

if [ "$ADD_PATH" = "y" ] || [ "$ADD_PATH" = "Y" ]; then
    QUILL_PATH="$SCRIPT_DIR"
    
    # Determine shell config file
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    
    # Check if already in PATH
    if ! grep -q "$SCRIPT_DIR" "$SHELL_CONFIG" 2>/dev/null; then
        echo "" >> "$SHELL_CONFIG"
        echo "# Quill Programming Language" >> "$SHELL_CONFIG"
        echo "export PATH=\"\$PATH:$QUILL_PATH\"" >> "$SHELL_CONFIG"
        echo -e "${GREEN}✓ Added to PATH in $SHELL_CONFIG${NC}"
        echo -e "${YELLOW}  Run 'source $SHELL_CONFIG' to use 'quill' command${NC}"
    else
        echo -e "${GREEN}✓ Already in PATH${NC}"
    fi
fi

echo ""

# VS Code extension setup (optional)
echo -e "${YELLOW}Setting up VS Code extension...${NC}"

if command -v code &> /dev/null; then
    EXTENSIONS_JSON="$SCRIPT_DIR/.vscode/extensions.json"
    
    if [ -f "$EXTENSIONS_JSON" ]; then
        echo -e "${GREEN}✓ VS Code detected! Extension will auto-install when you open this workspace${NC}"
        echo -e "  ${YELLOW}(Configured in .vscode/extensions.json)${NC}"
    else
        echo -e "${YELLOW}⚠ Extension configuration not found${NC}"
        echo -e "  ${YELLOW}You may need to manually install from tools/vscode-extension/${NC}"
    fi
else
    echo -e "${YELLOW}🟡 VS Code not detected (optional)${NC}"
    echo -e "  ${YELLOW}Quill works without VS Code! You can use any text editor.${NC}"
    echo -e "  ${YELLOW}Install VS Code for syntax highlighting: https://code.visualstudio.com/${NC}"
fi

echo ""
echo "========================================"
echo -e "${GREEN}    Installation Complete! 🎉${NC}"
echo "========================================"
echo ""

# Show next steps
echo -e "${YELLOW}Next Steps:${NC}"
echo -e "  1. Run a demo: ${NC}./quill examples/example_simple.quill"
echo -e "  2. Open workspace in VS Code for syntax highlighting"
echo -e "  3. Read the docs: ${NC}README.md and docs/"
echo ""

echo -e "For help, visit: ${CYAN}https://github.com/yourusername/quill${NC}"
echo ""

# Test installation
echo -e "${YELLOW}Testing installation...${NC}"
TEST_FILE="$SCRIPT_DIR/examples/example_simple.quill"
LAUNCHER="$SCRIPT_DIR/quill"

if [ -f "$TEST_FILE" ] && [ -f "$LAUNCHER" ]; then
    echo -e "  ${YELLOW}Running test program...${NC}"
    "$LAUNCHER" "$TEST_FILE"
    echo ""
    echo -e "${GREEN}✓ Installation test successful!${NC}"
else
    echo -e "  ${YELLOW}⚠ Test file not found, but installation completed${NC}"
fi

echo ""
echo -e "${CYAN}Happy coding with Quill! ✨${NC}"
echo ""
