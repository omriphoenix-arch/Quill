"""
Standard library functions for Quill
Common utility functions available to all scripts
"""

import random
import math

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


def get_stdlib_functions():
    """Return dictionary of all stdlib functions for interpreter"""
    stdlib = QuillStdlib()
    return {
        # Math utilities
        'clamp': stdlib.clamp,
        'min': stdlib.min_val,
        'max': stdlib.max_val,
        'sum': stdlib.sum_val,
        'average': stdlib.average,
        'avg': stdlib.average,  # Alias
        'round': stdlib.round_val,
        'floor': stdlib.floor,
        'ceil': stdlib.ceil,
        'sqrt': stdlib.sqrt,
        'pow': stdlib.pow_val,
        
        # Random
        'random_choice': stdlib.random_choice,
        'random_int': stdlib.random_int,
        'random_float': stdlib.random_float,
        'choice': stdlib.random_choice,  # Alias
        
        # String utilities
        'trim': stdlib.trim,
        'lower': stdlib.lower,
        'upper': stdlib.upper,
        'capitalize': stdlib.capitalize,
        'title': stdlib.title,
        'split': stdlib.split,
        'join': stdlib.join,
        'replace': stdlib.replace,
        'starts_with': stdlib.starts_with,
        'ends_with': stdlib.ends_with,
        'contains': stdlib.contains,
        
        # List utilities
        'reverse': stdlib.reverse,
        'sort': stdlib.sort,
        
        # Type checking
        'is_number': stdlib.is_number,
        'is_string': stdlib.is_string,
        'is_list': stdlib.is_list,
        'is_empty': stdlib.is_empty,
    }
