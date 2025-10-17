"""
Interpreter for Quill
Executes the AST
"""

from parser import *
from gui_engine import GUIEngine
from colors import *
import math
import random
import json
import os
import time
import sys

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Function:
    def __init__(self, name, parameters, body, closure):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.closure = closure

class Interpreter:
    def __init__(self, source="", legacy_mode=False):
        self.variables = {}
        self.functions = {}
        self.labels = {}
        self.statements = []
        self.current_pos = 0
        self.inventory = []  # Player's inventory
        self.gui = GUIEngine(interpreter=self)  # GUI engine for desktop apps
        self.source = source  # Store source for error context
        self.legacy_mode = legacy_mode  # Auto-import game/io in legacy mode
        
        # Import standard library
        from stdlib import get_stdlib_functions
        
        # Built-in functions (CORE ONLY - no game/io by default)
        self.builtins = {
            # Basic type functions
            'len': lambda x: len(x),
            'str': lambda x: str(x),
            'int': lambda x: int(x),
            'float': lambda x: float(x),
            'type': lambda x: type(x).__name__,
            'range': lambda *args: list(range(*args)),
            'abs': lambda x: abs(x),
        }
        
        # Add stdlib functions (pass interpreter to allow rich error wrapping)
        try:
            self.builtins.update(get_stdlib_functions(self))
        except Exception:
            # Fallback if stdlib import fails for any reason
            try:
                self.builtins.update(get_stdlib_functions())
            except Exception:
                pass
        
        # Initialize module system
        try:
            from modules import ModuleLoader
            self.module_loader = ModuleLoader(self)
        except Exception as e:
            print(f"Warning: Could not initialize module system: {e}")
            self.module_loader = None
        
        # Legacy mode: auto-import game and io modules
        if self.legacy_mode and self.module_loader:
            try:
                self.module_loader.import_from('game', '*')
                self.module_loader.import_from('io', '*')
            except Exception:
                pass
    
    def runtime_error(self, message, node=None, hint=None):
        """Raise a rich runtime error with context"""
        from errors import QuillRuntimeError, get_hint
        line = getattr(node, 'line', 0) if node else 0
        column = getattr(node, 'column', 0) if node else 0
        source_lines = self.source.split('\n')
        source_line = source_lines[line - 1] if line <= len(source_lines) else ""
        raise QuillRuntimeError(
            message,
            line=line,
            column=column,
            source_line=source_line,
            hint=hint or get_hint(message)
        )
    
    def run(self, statements):
        self.statements = statements
        
        # First pass: collect all labels
        for i, stmt in enumerate(statements):
            if isinstance(stmt, LabelNode):
                self.labels[stmt.name] = i
        
        # Second pass: execute statements
        self.current_pos = 0
        while self.current_pos < len(self.statements):
            stmt = self.statements[self.current_pos]
            self.execute(stmt)
            self.current_pos += 1
        
        # If GUI was used, keep window open
        if self.gui.window is not None:
            self.gui.run_mainloop()
    
    def execute(self, node):
        if isinstance(node, SayNode):
            value = self.evaluate(node.expression)
            # Color the output in cyan for story text
            print(colorize(str(value), Colors.CYAN))
        
        elif isinstance(node, AskNode):
            prompt = self.evaluate(node.prompt)
            # Color the prompt in yellow with a nice arrow
            colored_prompt = colorize(f"❓ {prompt}", Colors.BRIGHT_YELLOW)
            try:
                user_input = input(colored_prompt + colorize(" ➤ ", Colors.BRIGHT_GREEN))
                self.variables[node.variable] = user_input
            except EOFError:
                print(colorize("\n\n⚠ Input ended unexpectedly. Exiting program.", Colors.YELLOW))
                exit(0)
        
        elif isinstance(node, SetNode):
            value = self.evaluate(node.expression)
            if isinstance(node.variable, str):
                self.variables[node.variable] = value
            elif isinstance(node.variable, IndexNode):
                # Handle list/string indexing assignment
                obj = self.evaluate(node.variable.object)
                index = self.evaluate(node.variable.index)
                if isinstance(obj, list):
                    obj[int(index)] = value
                else:
                    raise RuntimeError(f"Cannot index assign to {type(obj).__name__}")
            else:
                raise RuntimeError(f"Invalid assignment target")
        
        elif isinstance(node, IfNode):
            condition = self.evaluate(node.condition)
            if self.is_truthy(condition):
                for stmt in node.then_block:
                    self.execute(stmt)
            elif node.else_block:
                for stmt in node.else_block:
                    self.execute(stmt)
        
        elif isinstance(node, WhileNode):
            while self.is_truthy(self.evaluate(node.condition)):
                try:
                    for stmt in node.body:
                        self.execute(stmt)
                except BreakException:
                    break
                except ContinueException:
                    continue
        
        elif isinstance(node, ForNode):
            iterable = self.evaluate(node.iterable)
            if not hasattr(iterable, '__iter__'):
                raise RuntimeError(f"Cannot iterate over {type(iterable).__name__}")
            
            for item in iterable:
                self.variables[node.variable] = item
                try:
                    for stmt in node.body:
                        self.execute(stmt)
                except BreakException:
                    break
                except ContinueException:
                    continue
        
        elif isinstance(node, FunctionNode):
            # Store function definition
            func = Function(node.name, node.parameters, node.body, dict(self.variables))
            self.functions[node.name] = func
        
        elif isinstance(node, ReturnNode):
            value = self.evaluate(node.expression) if node.expression else None
            raise ReturnException(value)
        
        elif isinstance(node, FunctionCallNode):
            # Execute as statement (ignore return value)
            self.evaluate(node)
        
        elif isinstance(node, BreakNode):
            raise BreakException()
        
        elif isinstance(node, ContinueNode):
            raise ContinueException()
        
        elif isinstance(node, ImportNode):
            # Handle import statements
            if self.module_loader is None:
                raise RuntimeError("Module system not available")
            
            try:
                if node.from_import:
                    # from module import ...
                    self.module_loader.import_from(node.module_name, node.import_names)
                    if '*' in node.import_names:
                        print(f"✓ Imported all from '{node.module_name}'")
                    else:
                        print(f"✓ Imported {', '.join(node.import_names)} from '{node.module_name}'")
                else:
                    # import module
                    self.module_loader.import_module(node.module_name, into_globals=False)
                    print(f"✓ Loaded module '{node.module_name}'")
            except Exception as e:
                self.runtime_error(f"Failed to import module '{node.module_name}': {e}", node)
        
        elif isinstance(node, ChoiceNode):
            # Styled choice menu
            print(f"\n{colorize('╔═══════════════════════════════╗', Colors.BRIGHT_BLUE)}")
            print(f"{colorize('║', Colors.BRIGHT_BLUE)} {colorize('Choose an option:', Colors.BOLD + Colors.BRIGHT_CYAN)}          {colorize('║', Colors.BRIGHT_BLUE)}")
            print(f"{colorize('╚═══════════════════════════════╝', Colors.BRIGHT_BLUE)}")
            
            options_list = []
            for i, option in enumerate(node.options, 1):
                option_text = self.evaluate(option)
                options_list.append(option_text)
                # Colorful option list
                number = colorize(f"{i}.", Colors.BRIGHT_YELLOW)
                text = colorize(option_text, Colors.CYAN)
                print(f"  {number} {text}")
            
            while True:
                try:
                    prompt = colorize("\n➤ Enter your choice (number): ", Colors.BRIGHT_GREEN)
                    choice = input(prompt)
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(options_list):
                        selected = options_list[choice_num - 1]
                        self.variables['answer'] = selected
                        print(success(f"You chose: {selected}"))
                        break
                    else:
                        print(warning(f"Please enter a number between 1 and {len(options_list)}"))
                except ValueError:
                    print(error("Please enter a valid number"))
                except EOFError:
                    print(colorize("\n\n⚠ Input ended unexpectedly. Exiting program.", Colors.YELLOW))
                    exit(0)
        
        elif isinstance(node, GotoNode):
            if node.label in self.labels:
                self.current_pos = self.labels[node.label] - 1  # -1 because it will be incremented
            else:
                raise RuntimeError(f"Label '{node.label}' not found")
        
        elif isinstance(node, LabelNode):
            pass  # Labels are just markers, nothing to execute
        
        # GUI Nodes
        elif isinstance(node, WindowNode):
            title = self.evaluate(node.title)
            props = self._evaluate_properties(node.properties)
            self.gui.create_window(title, props)
        
        elif isinstance(node, ButtonNode):
            text = self.evaluate(node.text)
            props = self._evaluate_properties(node.properties)
            self.gui.create_button(text, props)
        
        elif isinstance(node, TextboxNode):
            text = self.evaluate(node.text)
            props = self._evaluate_properties(node.properties)
            self.gui.create_textbox(text, props)
        
        elif isinstance(node, ImageNode):
            filepath = self.evaluate(node.filepath)
            props = self._evaluate_properties(node.properties)
            self.gui.create_image(filepath, props)
        
        elif isinstance(node, GUILabelNode):
            text = self.evaluate(node.text)
            props = self._evaluate_properties(node.properties)
            self.gui.create_label(text, props)
        
        elif isinstance(node, InputNode):
            props = self._evaluate_properties(node.properties)
            self.gui.create_input(node.variable, props)
        
        elif isinstance(node, ShowNode):
            self.gui.show_window()
        
        elif isinstance(node, HideNode):
            self.gui.hide_window()
        
        elif isinstance(node, UpdateNode):
            widget_id = node.widget_id
            new_text = self.evaluate(node.new_text)
            self.gui.update_textbox(widget_id, new_text)
    
    def evaluate(self, node):
        if isinstance(node, LiteralNode):
            return node.value
        
        elif isinstance(node, VariableNode):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                self.runtime_error(f"Variable '{node.name}' is not defined", node, "Make sure the variable is declared with 'set' before using it")
        
        elif isinstance(node, BinaryOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            
            if node.operator == '+':
                # Smart addition: numbers add, strings concatenate
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left + right
                else:
                    return str(left) + str(right)
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                if right == 0:
                    self.runtime_error("Division by zero", node, "Check that the divisor is not zero before dividing")
                return left / right
            elif node.operator == '%':
                return left % right
            elif node.operator == '**':
                return left ** right
            elif node.operator == '==':
                return left == right
            elif node.operator == '!=':
                return left != right
            elif node.operator == '>':
                return left > right
            elif node.operator == '<':
                return left < right
            elif node.operator == '>=':
                return left >= right
            elif node.operator == '<=':
                return left <= right
            elif node.operator == 'and':
                return self.is_truthy(left) and self.is_truthy(right)
            elif node.operator == 'or':
                return self.is_truthy(left) or self.is_truthy(right)
        
        elif isinstance(node, UnaryOpNode):
            operand = self.evaluate(node.operand)
            if node.operator == 'not':
                return not self.is_truthy(operand)
            elif node.operator == '-':
                return -operand
        
        elif isinstance(node, ListNode):
            return [self.evaluate(elem) for elem in node.elements]
        
        elif isinstance(node, IndexNode):
            obj = self.evaluate(node.object)
            index = self.evaluate(node.index)
            
            if isinstance(obj, (list, str)):
                try:
                    return obj[int(index)]
                except IndexError:
                    self.runtime_error(f"Index {index} out of range for {type(obj).__name__} of length {len(obj)}", node, "Array/string indices must be within bounds (0 to length-1)")
            else:
                self.runtime_error(f"Cannot index {type(obj).__name__}", node)
        
        elif isinstance(node, FunctionCallNode):
            # Check built-in functions first
            if node.name in self.builtins:
                args = [self.evaluate(arg) for arg in node.arguments]
                try:
                    return self.builtins[node.name](*args)
                except Exception as e:
                    raise RuntimeError(f"Error calling built-in function '{node.name}': {e}")
            
            # Check user-defined functions
            elif node.name in self.functions:
                func = self.functions[node.name]
                
                if len(node.arguments) != len(func.parameters):
                    raise RuntimeError(f"Function '{node.name}' expects {len(func.parameters)} arguments, got {len(node.arguments)}")
                
                # Evaluate arguments in current scope
                arg_values = [self.evaluate(arg) for arg in node.arguments]
                
                # Save current variables
                saved_vars = dict(self.variables)
                
                # Set up function scope with closure
                self.variables = dict(func.closure)
                
                # Bind arguments to parameters
                for param, value in zip(func.parameters, arg_values):
                    self.variables[param] = value
                
                # Execute function body
                return_value = None
                try:
                    for stmt in func.body:
                        self.execute(stmt)
                except ReturnException as e:
                    return_value = e.value
                
                # Restore variables
                self.variables = saved_vars
                return return_value
            else:
                raise RuntimeError(f"Function '{node.name}' is not defined")
        
        return None
    
    def is_truthy(self, value):
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, str):
            return len(value) > 0
        return False
    
    # Timing Functions
    def _wait(self, seconds):
        """Pause execution for the specified number of seconds"""
        try:
            delay = float(seconds)
            if delay > 0:
                time.sleep(delay)
                return True
            return False
        except (ValueError, TypeError):
            print(f"✗ Error: wait() requires a number, got {seconds}")
            return False
    
    # Inventory System Methods
    def _add_item(self, item):
        """Add an item to the inventory"""
        item_name = str(item)
        self.inventory.append(item_name)
        print(f"✓ Added '{item_name}' to inventory")
        return True
    
    def _remove_item(self, item):
        """Remove an item from the inventory"""
        item_name = str(item)
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            print(f"✓ Removed '{item_name}' from inventory")
            return True
        else:
            print(f"✗ '{item_name}' not found in inventory")
            return False
    
    def _has_item(self, item):
        """Check if inventory contains an item"""
        item_name = str(item)
        return item_name in self.inventory
    
    def _show_inventory(self):
        """Display the inventory"""
        print("\n" + "="*40)
        print("          INVENTORY")
        print("="*40)
        
        if not self.inventory:
            print("  (Empty)")
        else:
            # Count duplicate items
            item_counts = {}
            for item in self.inventory:
                item_counts[item] = item_counts.get(item, 0) + 1
            
            # Display items
            for item, count in item_counts.items():
                if count > 1:
                    print(f"  • {item} (x{count})")
                else:
                    print(f"  • {item}")
        
        print("="*40)
        print(f"Total items: {len(self.inventory)}")
        print("="*40 + "\n")
        return None
    
    def _clear_inventory(self):
        """Clear all items from inventory"""
        self.inventory.clear()
        print("✓ Inventory cleared")
        return True
    
    # Save/Load System Methods
    def _save_game(self, filename):
        """Save the current game state to a file"""
        try:
            # Ensure .save extension
            if not str(filename).endswith('.save'):
                filename = str(filename) + '.save'
            
            # Create saves directory if it doesn't exist
            saves_dir = 'saves'
            if not os.path.exists(saves_dir):
                os.makedirs(saves_dir)
            
            filepath = os.path.join(saves_dir, filename)
            
            # Prepare save data
            save_data = {
                'variables': {},
                'inventory': self.inventory.copy()
            }
            
            # Save only serializable variables
            for key, value in self.variables.items():
                if isinstance(value, (int, float, str, bool, list, dict, type(None))):
                    save_data['variables'][key] = value
            
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=2)
            
            print(f"💾 Game saved to: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error saving game: {e}")
            return False
    
    def _load_game(self, filename):
        """Load a saved game state from a file"""
        try:
            # Ensure .save extension
            if not str(filename).endswith('.save'):
                filename = str(filename) + '.save'
            
            filepath = os.path.join('saves', filename)
            
            # Check if file exists
            if not os.path.exists(filepath):
                print(f"❌ Save file not found: {filepath}")
                return False
            
            # Read save file
            with open(filepath, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            # Restore variables
            self.variables.update(save_data.get('variables', {}))
            
            # Restore inventory
            self.inventory = save_data.get('inventory', [])
            
            print(f"✓ Game loaded from: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading game: {e}")
            return False
    
    def _has_save(self, filename):
        """Check if a save file exists"""
        # Ensure .save extension
        if not str(filename).endswith('.save'):
            filename = str(filename) + '.save'
        
        filepath = os.path.join('saves', filename)
        return os.path.exists(filepath)
    
    def _delete_save(self, filename):
        """Delete a save file"""
        try:
            # Ensure .save extension
            if not str(filename).endswith('.save'):
                filename = str(filename) + '.save'
            
            filepath = os.path.join('saves', filename)
            
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"✓ Deleted save file: {filepath}")
                return True
            else:
                print(f"❌ Save file not found: {filepath}")
                return False
                
        except Exception as e:
            print(f"❌ Error deleting save: {e}")
            return False
    
    def _evaluate_properties(self, properties):
        """Evaluate all property values (convert AST nodes to actual values)"""
        evaluated = {}
        for key, value in properties.items():
            # Special handling for onclick and id - they're already strings, don't evaluate
            if key in ['onclick', 'id']:
                evaluated[key] = value
            # Check if value is an AST node
            elif hasattr(value, '__class__') and hasattr(value.__class__, '__bases__'):
                # Try to evaluate as an expression
                try:
                    evaluated[key] = self.evaluate(value)
                except:
                    evaluated[key] = value
            else:
                evaluated[key] = value
        return evaluated
