"""
I/O Module for Quill
File input/output operations
"""

def get_io_functions(interpreter=None):
    """
    Return dictionary of I/O functions
    
    If interpreter is provided, errors will be wrapped as QuillRuntimeError
    """
    import os
    
    def wrap_error(name, fn):
        """Wrap function to convert exceptions to QuillRuntimeError"""
        if interpreter is None:
            return fn
        
        def wrapped(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                try:
                    interpreter.runtime_error(f"Error in io.{name}: {e}")
                except:
                    raise
        return wrapped
    
    def read_text(path):
        """Read entire text file and return as string"""
        with open(str(path), 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_text(path, content):
        """Write text to a file (overwrites). Creates parent dirs if needed."""
        path = str(path)
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(content))
        return True
    
    def append_text(path, content):
        """Append text to a file. Creates parent dirs if needed."""
        path = str(path)
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(str(content))
        return True
    
    def read_lines(path):
        """Read a file and return a list of lines (without trailing newlines)"""
        with open(str(path), 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f.readlines()]
    
    def write_lines(path, lines):
        """Write an iterable of lines to a file. Each item will become a line."""
        path = str(path)
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            for item in lines:
                f.write(str(item) + '\n')
        return True
    
    def file_exists(path):
        """Check if a file exists"""
        return os.path.exists(str(path))
    
    def delete_file(path):
        """Delete a file"""
        if os.path.exists(str(path)):
            os.remove(str(path))
            return True
        return False
    
    def list_files(directory="."):
        """List files in a directory"""
        return [f for f in os.listdir(str(directory)) if os.path.isfile(os.path.join(str(directory), f))]
    
    def create_directory(path):
        """Create a directory (and parents if needed)"""
        os.makedirs(str(path), exist_ok=True)
        return True
    
    return {
        'read_text': wrap_error('read_text', read_text),
        'write_text': wrap_error('write_text', write_text),
        'append_text': wrap_error('append_text', append_text),
        'read_lines': wrap_error('read_lines', read_lines),
        'write_lines': wrap_error('write_lines', write_lines),
        'file_exists': wrap_error('file_exists', file_exists),
        'delete_file': wrap_error('delete_file', delete_file),
        'list_files': wrap_error('list_files', list_files),
        'create_directory': wrap_error('create_directory', create_directory),
    }
