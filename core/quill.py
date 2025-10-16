"""
Quill - A Beginner-Friendly Programming Language
Main entry point for the interpreter
"""

import sys
import io

# Fix Unicode encoding issues on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from colors import *

def run_file(filename):
    try:
        # Show mini banner
        print(divider('═', 60, Colors.BRIGHT_MAGENTA))
        print(colorize(f"  📖 Running: {filename}", Colors.BRIGHT_CYAN))
        print(divider('═', 60, Colors.BRIGHT_MAGENTA))
        print()
        
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Lexing
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Interpreting
        interpreter = Interpreter()
        interpreter.run(ast)
        
        # Success message
        print()
        print(divider('═', 60, Colors.BRIGHT_MAGENTA))
        print(success("Story completed successfully!"))
        print(divider('═', 60, Colors.BRIGHT_MAGENTA))
        
    except FileNotFoundError:
        print(error(f"File '{filename}' not found"))
        sys.exit(1)
    except SyntaxError as e:
        print(error(f"Syntax Error: {e}"))
        sys.exit(1)
    except RuntimeError as e:
        print(error(f"Runtime Error: {e}"))
        sys.exit(1)
    except Exception as e:
        print(error(f"Error: {e}"))
        sys.exit(1)

def run_interactive():
    print("StoryScript Interactive Mode")
    print("Type your code and press Ctrl+D (Unix) or Ctrl+Z (Windows) when done\n")
    
    lines = []
    try:
        while True:
            line = input(">>> " if not lines else "... ")
            lines.append(line)
    except EOFError:
        pass
    
    source = '\n'.join(lines)
    
    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        interpreter.run(ast)
        
    except (SyntaxError, RuntimeError) as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        # Show logo
        print_logo()
        print(colorize("Usage:", Colors.BOLD + Colors.BRIGHT_YELLOW))
        print(colorize("  quill <filename.quill>", Colors.BRIGHT_CYAN) + "  - Run a Quill program")
        print()
        print(colorize("Examples:", Colors.BOLD + Colors.BRIGHT_YELLOW))
        print(colorize("  quill adventure.quill", Colors.BRIGHT_GREEN))
        print(colorize("  quill examples/demo.quill", Colors.BRIGHT_GREEN))
        print()
        sys.exit(0)
    
    filename = sys.argv[1]
    run_file(filename)

if __name__ == "__main__":
    main()
