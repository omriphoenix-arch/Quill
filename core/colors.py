"""
Terminal Color and Formatting Utilities for Quill
Provides ANSI color codes and styled output
"""

import os
import sys

# Enable ANSI colors on Windows
if sys.platform == 'win32':
    # Method 1: Empty command to enable ANSI
    os.system('')
    
    # Method 2: Use Windows API to enable virtual terminal processing
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Get the current console mode
        console_handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(console_handle, ctypes.byref(mode))
        # Enable virtual terminal processing (0x0004)
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        kernel32.SetConsoleMode(console_handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    except:
        pass  # If this fails, fall back to os.system method

class Colors:
    """ANSI color codes for terminal output"""
    
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Semantic colors
    SUCCESS = '\033[92m'  # Bright green
    ERROR = '\033[91m'    # Bright red
    WARNING = '\033[93m'  # Bright yellow
    INFO = '\033[96m'     # Bright cyan
    STORY = '\033[95m'    # Bright magenta
    CHOICE = '\033[94m'   # Bright blue
    INPUT = '\033[93m'    # Bright yellow

def colorize(text, color):
    """Wrap text in ANSI color code"""
    return f"{color}{text}{Colors.RESET}"

def bold(text):
    """Make text bold"""
    return f"{Colors.BOLD}{text}{Colors.RESET}"

def italic(text):
    """Make text italic"""
    return f"{Colors.ITALIC}{text}{Colors.RESET}"

def underline(text):
    """Underline text"""
    return f"{Colors.UNDERLINE}{text}{Colors.RESET}"

def success(text):
    """Format success message"""
    return f"{Colors.SUCCESS}✓ {text}{Colors.RESET}"

def error(text):
    """Format error message"""
    return f"{Colors.ERROR}✗ {text}{Colors.RESET}"

def warning(text):
    """Format warning message"""
    return f"{Colors.WARNING}⚠ {text}{Colors.RESET}"

def info(text):
    """Format info message"""
    return f"{Colors.INFO}ℹ {text}{Colors.RESET}"

def story(text):
    """Format story text"""
    return f"{Colors.STORY}{text}{Colors.RESET}"

def box(text, width=60, color=Colors.CYAN):
    """Create a box around text"""
    lines = text.split('\n')
    horizontal = '═' * (width - 2)
    
    result = [f"{color}╔{horizontal}╗{Colors.RESET}"]
    for line in lines:
        padding = width - len(line) - 4
        result.append(f"{color}║{Colors.RESET} {line}{' ' * padding} {color}║{Colors.RESET}")
    result.append(f"{color}╚{horizontal}╝{Colors.RESET}")
    
    return '\n'.join(result)

def banner(text, color=Colors.BRIGHT_CYAN):
    """Create a stylish banner"""
    width = len(text) + 4
    horizontal = '=' * width
    
    return f"""
{color}{horizontal}
  {text}
{horizontal}{Colors.RESET}
"""

def progress_bar(current, total, width=50, color=Colors.GREEN):
    """Create a progress bar"""
    percent = current / total
    filled = int(width * percent)
    empty = width - filled
    
    bar = '█' * filled + '░' * empty
    percentage = int(percent * 100)
    
    return f"{color}[{bar}] {percentage}%{Colors.RESET}"

def choice_list(options):
    """Format a list of choices"""
    result = [f"\n{Colors.CHOICE}{Colors.BOLD}Choose an option:{Colors.RESET}"]
    for i, option in enumerate(options, 1):
        result.append(f"{Colors.BRIGHT_YELLOW}{i}.{Colors.RESET} {Colors.CYAN}{option}{Colors.RESET}")
    return '\n'.join(result)

def divider(char='─', width=60, color=Colors.BRIGHT_BLACK):
    """Create a divider line"""
    return f"{color}{char * width}{Colors.RESET}"

def rainbow(text):
    """Make text rainbow colored"""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    result = ""
    for i, char in enumerate(text):
        if char != ' ':
            result += colors[i % len(colors)] + char
        else:
            result += char
    return result + Colors.RESET

def gradient(text, start_color, end_color):
    """Create a gradient effect (simplified version)"""
    # For simplicity, just alternate between two colors
    result = ""
    mid = len(text) // 2
    for i, char in enumerate(text):
        if char != ' ':
            color = start_color if i < mid else end_color
            result += color + char
        else:
            result += char
    return result + Colors.RESET

# ASCII Art for Quill logo
LOGO = f"""{Colors.BRIGHT_MAGENTA}
    ____        _ ____
   / __ \\__  __(_) / /
  / / / / / / / / / / 
 / /_/ / /_/ / / / /  
 \\___\\_\\__,_/_/_/_/   
                      
{Colors.RESET}"""

MINI_LOGO = f"""{Colors.BRIGHT_CYAN}
╔═══════════════════════════════╗
║      {Colors.BRIGHT_MAGENTA}Quill{Colors.BRIGHT_CYAN} Programming      ║
║   {Colors.BRIGHT_YELLOW}Write Code Like a Story{Colors.BRIGHT_CYAN}   ║
╚═══════════════════════════════╝
{Colors.RESET}"""

def print_logo():
    """Print the Quill logo"""
    print(LOGO)
    print(colorize("    Write Your Programs Like Stories", Colors.BRIGHT_CYAN))
    print(colorize("    Version 1.0.0-beta", Colors.BRIGHT_BLACK))
    print()
