"""
Standard library functions for Quill
Common utility functions available to all scripts
"""

import random
import math
import os

from typing import Iterable

class QuillStdlib:
    """Standard library functions for Quill"""
    
    @staticmethod
    def clamp(value, min_val, max_val):
        """Clamp a value between min and max"""
        return max(min_val, min(max_val, value))
    
    @staticmethod
    def random_choice(*items):
        """Pick a random item from the arguments"""
        return random.choice(items) if items else None
    
    @staticmethod
    def random_int(min_val, max_val):
        """Generate a random integer between min and max (inclusive)"""
        return random.randint(int(min_val), int(max_val))
    
    @staticmethod
    def random_float():
        """Generate a random float between 0.0 and 1.0"""
        return random.random()
    
    @staticmethod
    def trim(s):
        """Remove whitespace from both ends of a string"""
        return str(s).strip()
    
    @staticmethod
    def lower(s):
        """Convert string to lowercase"""
        return str(s).lower()
    
    @staticmethod
    def upper(s):
        """Convert string to uppercase"""
        return str(s).upper()
    
    @staticmethod
    def capitalize(s):
        """Capitalize first letter of string"""
        return str(s).capitalize()
    
    @staticmethod
    def title(s):
        """Convert string to title case"""
        return str(s).title()
    
    @staticmethod
    def split(s, delimiter=" "):
        """Split string by delimiter (default: space)"""
        return str(s).split(delimiter)
    
    @staticmethod
    def join(items, separator=""):
        """Join list items into a string with separator"""
        return separator.join(str(item) for item in items)
    
    @staticmethod
    def replace(s, old, new):
        """Replace occurrences of old with new in string"""
        return str(s).replace(old, new)
    
    @staticmethod
    def starts_with(s, prefix):
        """Check if string starts with prefix"""
        return str(s).startswith(prefix)
    
    @staticmethod
    def ends_with(s, suffix):
        """Check if string ends with suffix"""
        return str(s).endswith(suffix)
    
    @staticmethod
    def contains(s, substring):
        """Check if string contains substring"""
        return substring in str(s)
    
    @staticmethod
    def reverse(items):
        """Reverse a list or string"""
        if isinstance(items, str):
            return items[::-1]
        return list(reversed(items))
    
    @staticmethod
    def sort(items, reverse=False):
        """Sort a list"""
        return sorted(items, reverse=bool(reverse))
    
    @staticmethod
    def min_val(*items):
        """Return minimum value"""
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            return min(items[0])
        return min(items)
    
    @staticmethod
    def max_val(*items):
        """Return maximum value"""
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            return max(items[0])
        return max(items)
    
    @staticmethod
    def sum_val(*items):
        """Sum all numbers"""
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            return sum(items[0])
        return sum(items)
    
    @staticmethod
    def average(*items):
        """Calculate average of numbers"""
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            items = items[0]
        if not items:
            return 0
        return sum(items) / len(items)
    
    @staticmethod
    def round_val(number, decimals=0):
        """Round number to specified decimal places"""
        return round(number, int(decimals))
    
    @staticmethod
    def floor(number):
        """Round down to nearest integer"""
        return math.floor(number)
    
    @staticmethod
    def ceil(number):
        """Round up to nearest integer"""
        return math.ceil(number)
    
    @staticmethod
    def sqrt(number):
        """Square root"""
        return math.sqrt(number)
    
    @staticmethod
    def pow_val(base, exponent):
        """Power function"""
        return pow(base, exponent)
    
    @staticmethod
    def is_number(value):
        """Check if value is a number"""
        return isinstance(value, (int, float))
    
    @staticmethod
    def is_string(value):
        """Check if value is a string"""
        return isinstance(value, str)
    
    @staticmethod
    def is_list(value):
        """Check if value is a list"""
        return isinstance(value, list)
    
    @staticmethod
    def is_empty(value):
        """Check if value is empty (empty string, empty list, 0, None)"""
        if value is None:
            return True
        if isinstance(value, (str, list)):
            return len(value) == 0
        if isinstance(value, (int, float)):
            return value == 0
        return False

    # File I/O utilities
    @staticmethod
    def read_text(path):
        """Read entire text file and return as string"""
        with open(str(path), 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_text(path, content):
        """Write text to a file (overwrites). Creates parent dirs if needed."""
        path = str(path)
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(content))
        return True

    @staticmethod
    def append_text(path, content):
        """Append text to a file. Creates parent dirs if needed."""
        path = str(path)
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(str(content))
        return True

    @staticmethod
    def read_lines(path):
        """Read a file and return a list of lines (without trailing newlines)"""
        with open(str(path), 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f.readlines()]

    @staticmethod
    def write_lines(path, lines: Iterable):
        """Write an iterable of lines to a file. Each item will become a line."""
        path = str(path)
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            for item in lines:
                f.write(str(item) + '\n')
        return True


def get_stdlib_functions(interpreter=None):
    """Return dictionary of all stdlib functions for interpreter.

    If an Interpreter instance is provided, wrappers will convert exceptions
    into rich runtime errors via interpreter.runtime_error(message).
    """
    stdlib = QuillStdlib()

    def wrap(name, fn):
        if interpreter is None:
            return fn
        def wrapped(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                # Use interpreter's runtime_error to raise a QuillRuntimeError
                try:
                    interpreter.runtime_error(f"Error in stdlib function '{name}': {e}")
                except Exception:
                    # If runtime_error itself fails, fall back to raising the original exception
                    raise
        return wrapped

    return {
        # Math utilities
        'clamp': wrap('clamp', stdlib.clamp),
        'min': wrap('min', stdlib.min_val),
        'max': wrap('max', stdlib.max_val),
        'sum': wrap('sum', stdlib.sum_val),
        'average': wrap('average', stdlib.average),
        'avg': wrap('avg', stdlib.average),  # Alias
        'round': wrap('round', stdlib.round_val),
        'floor': wrap('floor', stdlib.floor),
        'ceil': wrap('ceil', stdlib.ceil),
        'sqrt': wrap('sqrt', stdlib.sqrt),
        'pow': wrap('pow', stdlib.pow_val),
        
        # Random
        'random_choice': wrap('random_choice', stdlib.random_choice),
        'random_int': wrap('random_int', stdlib.random_int),
        'random_float': wrap('random_float', stdlib.random_float),
        'choice': wrap('choice', stdlib.random_choice),  # Alias
        
        # String utilities
        'trim': wrap('trim', stdlib.trim),
        'lower': wrap('lower', stdlib.lower),
        'upper': wrap('upper', stdlib.upper),
        'capitalize': wrap('capitalize', stdlib.capitalize),
        'title': wrap('title', stdlib.title),
        'split': wrap('split', stdlib.split),
        'join': wrap('join', stdlib.join),
        'replace': wrap('replace', stdlib.replace),
        'starts_with': wrap('starts_with', stdlib.starts_with),
        'ends_with': wrap('ends_with', stdlib.ends_with),
        'contains': wrap('contains', stdlib.contains),
        
        # File I/O
        'read_text': wrap('read_text', stdlib.read_text),
        'write_text': wrap('write_text', stdlib.write_text),
        'append_text': wrap('append_text', stdlib.append_text),
        'read_lines': wrap('read_lines', stdlib.read_lines),
        'write_lines': wrap('write_lines', stdlib.write_lines),
        
        # List utilities
        'reverse': wrap('reverse', stdlib.reverse),
        'sort': wrap('sort', stdlib.sort),
        
        # Type checking
        'is_number': wrap('is_number', stdlib.is_number),
        'is_string': wrap('is_string', stdlib.is_string),
        'is_list': wrap('is_list', stdlib.is_list),
        'is_empty': wrap('is_empty', stdlib.is_empty),
    }
