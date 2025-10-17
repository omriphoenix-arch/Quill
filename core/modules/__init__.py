"""
Quill Module System
Manages loading and registration of modules
"""

class ModuleLoader:
    """Manages module loading and caching"""
    
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.loaded_modules = {}
        self.module_namespaces = {}
    
    def load_module(self, module_name):
        """Load a module by name"""
        if module_name in self.loaded_modules:
            return self.loaded_modules[module_name]
        
        if module_name == 'io':
            from .io_module import get_io_functions
            functions = get_io_functions(self.interpreter)
            self.loaded_modules[module_name] = functions
            return functions
        
        elif module_name == 'game':
            from .game_module import get_game_functions
            functions = get_game_functions(self.interpreter)
            self.loaded_modules[module_name] = functions
            return functions
        
        else:
            raise RuntimeError(f"Unknown module: {module_name}")
    
    def import_module(self, module_name, into_globals=False):
        """Import a module into namespace"""
        functions = self.load_module(module_name)
        
        if into_globals:
            # Direct import: add to interpreter builtins
            self.interpreter.builtins.update(functions)
        else:
            # Namespaced import: create module namespace
            self.module_namespaces[module_name] = functions
        
        return functions
    
    def import_from(self, module_name, function_names):
        """Import specific functions from a module"""
        functions = self.load_module(module_name)
        
        if function_names == '*':
            # Wildcard import
            self.interpreter.builtins.update(functions)
        else:
            # Import specific functions
            for name in function_names:
                if name in functions:
                    self.interpreter.builtins[name] = functions[name]
                else:
                    raise RuntimeError(f"Function '{name}' not found in module '{module_name}'")
    
    def get_module_function(self, module_name, function_name):
        """Get a function from a loaded module (for namespaced access)"""
        if module_name not in self.module_namespaces:
            raise RuntimeError(f"Module '{module_name}' not imported")
        
        functions = self.module_namespaces[module_name]
        if function_name not in functions:
            raise RuntimeError(f"Function '{function_name}' not found in module '{module_name}'")
        
        return functions[function_name]


class ModuleNamespace:
    """Represents a module namespace for attribute access"""
    
    def __init__(self, name, functions):
        self.name = name
        self.functions = functions
    
    def __getattr__(self, name):
        if name in self.functions:
            return self.functions[name]
        raise AttributeError(f"Module '{self.name}' has no function '{name}'")
