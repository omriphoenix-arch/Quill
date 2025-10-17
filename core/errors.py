"""
Error utilities for Quill
Provides rich error formatting with source context, line/column, and caret pointers
"""

from typing import Optional
from colors import error as error_style

class QuillError(Exception):
    """Base class for Quill errors with rich context"""
    def __init__(self, message: str, line: int = 0, column: int = 0, 
                 source_line: Optional[str] = None, hint: Optional[str] = None):
        self.message = message
        self.line = line
        self.column = column
        self.source_line = source_line
        self.hint = hint
        super().__init__(self.format_error())
    
    def format_error(self) -> str:
        """Format error with context"""
        parts = []
        
        # Error header
        error_type = self.__class__.__name__.replace('Quill', '')
        if self.line > 0:
            parts.append(f"{error_style(error_type)} at line {self.line}, column {self.column}:")
        else:
            parts.append(f"{error_style(error_type)}:")
        
        parts.append(f"  {self.message}")
        
        # Source context with caret
        if self.source_line is not None and self.source_line.strip():
            parts.append("")
            parts.append(f"  {self.line:4d} | {self.source_line}")
            if self.column > 0:
                # Add caret pointer
                padding = len(f"  {self.line:4d} | ")
                caret_pos = padding + self.column - 1
                parts.append(" " * caret_pos + error_style("^"))
        
        # Optional hint
        if self.hint:
            parts.append("")
            parts.append(f"  💡 Hint: {self.hint}")
        
        return "\n".join(parts)

class QuillSyntaxError(QuillError):
    """Syntax errors during parsing"""
    pass

class QuillRuntimeError(QuillError):
    """Runtime errors during execution"""
    pass

class QuillTypeError(QuillError):
    """Type-related errors"""
    pass


def format_error_with_context(
    error_type: str,
    message: str,
    source: str,
    line: int,
    column: int = 0,
    hint: Optional[str] = None
) -> str:
    """
    Format an error message with source context
    
    Args:
        error_type: Type of error (Syntax, Runtime, etc.)
        message: Error description
        source: Full source code
        line: 1-indexed line number
        column: 1-indexed column number (0 = unknown)
        hint: Optional hint for fixing the error
    
    Returns:
        Formatted error string with context
    """
    lines = source.split('\n')
    source_line = lines[line - 1] if 0 < line <= len(lines) else None
    
    parts = []
    
    # Error header
    if line > 0:
        parts.append(f"{error_style(error_type + ' Error')} at line {line}, column {column}:")
    else:
        parts.append(f"{error_style(error_type + ' Error')}:")
    
    parts.append(f"  {message}")
    
    # Show surrounding context (line before and after)
    if source_line:
        parts.append("")
        
        # Line before (if exists)
        if line > 1:
            prev_line = lines[line - 2]
            parts.append(f"  {line-1:4d} | {prev_line}")
        
        # Error line with caret
        parts.append(f"  {line:4d} | {source_line}")
        if column > 0:
            padding = len(f"  {line:4d} | ")
            caret_pos = padding + column - 1
            parts.append(" " * caret_pos + error_style("^"))
        
        # Line after (if exists)
        if line < len(lines):
            next_line = lines[line]
            parts.append(f"  {line+1:4d} | {next_line}")
    
    # Optional hint
    if hint:
        parts.append("")
        parts.append(f"  💡 Hint: {hint}")
    
    return "\n".join(parts)


# Common hints for frequent errors
COMMON_HINTS = {
    "unterminated_string": "Strings must end with a closing quote mark (\") on the same line",
    "missing_then": "An 'if' statement requires 'then' before the body",
    "missing_end": "Control structures (if/while/for/function) must end with 'end'",
    "undefined_variable": "Make sure the variable is declared with 'set' before using it",
    "division_by_zero": "Check that the divisor is not zero before dividing",
    "invalid_index": "Array/string indices must be within bounds (0 to length-1)",
    "missing_do": "A 'while' loop requires 'do' before the body",
    "eof_in_string": "Strings cannot span multiple lines; close the string on the same line",
}


def get_hint(error_msg: str) -> Optional[str]:
    """Get a helpful hint based on error message patterns"""
    msg_lower = error_msg.lower()
    
    if "unterminated string" in msg_lower:
        return COMMON_HINTS["unterminated_string"]
    elif "expected then" in msg_lower or "missing then" in msg_lower:
        return COMMON_HINTS["missing_then"]
    elif "expected end" in msg_lower or "missing end" in msg_lower:
        return COMMON_HINTS["missing_end"]
    elif "not defined" in msg_lower or "undefined" in msg_lower:
        return COMMON_HINTS["undefined_variable"]
    elif "division by zero" in msg_lower:
        return COMMON_HINTS["division_by_zero"]
    elif "out of range" in msg_lower or "index" in msg_lower:
        return COMMON_HINTS["invalid_index"]
    elif "expected do" in msg_lower or "missing do" in msg_lower:
        return COMMON_HINTS["missing_do"]
    
    return None
