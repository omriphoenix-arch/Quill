"""
GUI Engine for Quill
Handles window creation and widget rendering using Tkinter
"""

import tkinter as tk
from tkinter import ttk, font as tkfont
from PIL import Image, ImageTk
import os

class GUIEngine:
    def __init__(self, interpreter=None):
        self.root = None
        self.window = None
        self.widgets = []
        self.theme = 'dark'
        self.button_callbacks = {}
        self.input_vars = {}
        self.interpreter = interpreter  # Reference to interpreter for callbacks
        self.named_widgets = {}  # Store widgets by ID for updates
        
        # Theme colors
        self.themes = {
            'dark': {
                'bg': '#1e1e1e',
                'fg': '#ffffff',
                'button_bg': '#0e639c',
                'button_fg': '#ffffff',
                'input_bg': '#3c3c3c',
                'input_fg': '#ffffff'
            },
            'light': {
                'bg': '#ffffff',
                'fg': '#000000',
                'button_bg': '#0078d4',
                'button_fg': '#ffffff',
                'input_bg': '#f0f0f0',
                'input_fg': '#000000'
            },
            'game': {
                'bg': '#1a1a2e',
                'fg': '#eee',
                'button_bg': '#16213e',
                'button_fg': '#0f3460',
                'input_bg': '#0f3460',
                'input_fg': '#eee'
            }
        }
    
    def create_window(self, title, properties=None):
        """Create main window"""
        if self.root is None:
            self.root = tk.Tk()
        
        self.window = self.root
        self.window.title(str(title))
        
        # Apply properties
        if properties:
            if 'theme' in properties and properties['theme'] is not None:
                self.theme = str(properties['theme'])
            
            if 'size' in properties and properties['size'] is not None:
                size = str(properties['size'])
                if size and size != 'None' and 'x' in size.lower():
                    # Parse "800x600" format
                    width, height = size.lower().split('x')
                    self.window.geometry(f"{width}x{height}")
                elif size and size != 'None':
                    self.window.geometry(size)
                else:
                    self.window.geometry("800x600")
            elif 'width' in properties and 'height' in properties:
                width = self.evaluate(properties['width'])
                height = self.evaluate(properties['height'])
                self.window.geometry(f"{width}x{height}")
            else:
                self.window.geometry("800x600")
            
            # Background color
            if self.theme and self.theme in self.themes:
                default_bg = self.themes[self.theme]['bg']
            else:
                self.theme = 'dark'
                default_bg = self.themes['dark']['bg']
            bgcolor = properties.get('bgcolor', default_bg)
            self.window.configure(bg=self.evaluate(bgcolor))
        else:
            self.window.geometry("800x600")
            self.window.configure(bg=self.themes[self.theme]['bg'])
        
        # Create canvas for absolute positioning
        self.canvas = tk.Canvas(
            self.window,
            bg=self.window.cget('bg'),
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        return self.window
    
    def create_button(self, text, properties=None):
        """Create a button widget"""
        if self.canvas is None:
            raise RuntimeError("Window must be created before adding widgets")
        
        text = str(self.evaluate(text))
        properties = properties or {}
        
        # Get theme colors
        theme = self.themes[self.theme]
        
        # Parse properties
        x = int(self.evaluate(properties.get('x', 100)))
        y = int(self.evaluate(properties.get('y', 100)))
        width = int(self.evaluate(properties.get('width', 120)))
        height = int(self.evaluate(properties.get('height', 40)))
        
        color = self.evaluate(properties.get('color', theme['button_fg']))
        bgcolor = self.evaluate(properties.get('bgcolor', theme['button_bg']))
        font_size = int(self.evaluate(properties.get('size', 12)))
        font_name = self.evaluate(properties.get('font', 'Arial'))
        
        # Create button
        button = tk.Button(
            self.canvas,
            text=text,
            bg=bgcolor,
            fg=color,
            font=(font_name, font_size, 'bold'),
            relief=tk.FLAT,
            cursor='hand2',
            borderwidth=0,
            padx=10,
            pady=5
        )
        
        # Handle onclick callback
        if 'onclick' in properties:
            callback_name = properties['onclick']
            button.configure(command=lambda: self.trigger_callback(callback_name))
        
        # Place button on canvas
        button_window = self.canvas.create_window(x, y, window=button, anchor='nw', width=width, height=height)
        
        self.widgets.append({
            'type': 'button',
            'widget': button,
            'window_id': button_window
        })
        
        return button
    
    def create_textbox(self, text, properties=None):
        """Create styled text label"""
        if self.canvas is None:
            raise RuntimeError("Window must be created before adding widgets")
        
        text = str(self.evaluate(text))
        properties = properties or {}
        
        theme = self.themes[self.theme]
        
        x = int(self.evaluate(properties.get('x', 100)))
        y = int(self.evaluate(properties.get('y', 50)))
        color = self.evaluate(properties.get('color', theme['fg']))
        bgcolor = self.evaluate(properties.get('bgcolor', theme['bg']))
        font_size = int(self.evaluate(properties.get('size', 16)))
        font_name = self.evaluate(properties.get('font', 'Arial'))
        align = properties.get('align', 'left')
        widget_id = properties.get('id', None)  # Optional ID for updates
        
        # Create label
        label = tk.Label(
            self.canvas,
            text=text,
            bg=bgcolor,
            fg=color,
            font=(font_name, font_size),
            justify=align
        )
        
        label_window = self.canvas.create_window(x, y, window=label, anchor='nw')
        
        widget_data = {
            'type': 'textbox',
            'widget': label,
            'window_id': label_window
        }
        
        self.widgets.append(widget_data)
        
        # Store by ID if provided
        if widget_id:
            self.named_widgets[widget_id] = widget_data
        
        return label
    
    def create_image(self, filepath, properties=None):
        """Load and display image"""
        if self.canvas is None:
            raise RuntimeError("Window must be created before adding widgets")
        
        filepath = str(self.evaluate(filepath))
        properties = properties or {}
        
        x = int(self.evaluate(properties.get('x', 0)))
        y = int(self.evaluate(properties.get('y', 0)))
        
        try:
            # Load image
            img = Image.open(filepath)
            
            # Resize if specified
            if 'width' in properties and 'height' in properties:
                width = int(self.evaluate(properties['width']))
                height = int(self.evaluate(properties['height']))
                img = img.resize((width, height), Image.Resampling.LANCZOS)
            elif 'size' in properties:
                size = str(properties['size'])
                if 'x' in size.lower():
                    width, height = map(int, size.lower().split('x'))
                    img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img)
            
            # Create image on canvas
            image_id = self.canvas.create_image(x, y, image=photo, anchor='nw')
            
            # Keep reference to prevent garbage collection
            self.widgets.append({
                'type': 'image',
                'image': photo,
                'image_id': image_id
            })
            
            return image_id
        except Exception as e:
            print(f"Error loading image {filepath}: {e}")
            return None
    
    def create_label(self, text, properties=None):
        """Create a simple label (similar to textbox but simpler)"""
        return self.create_textbox(text, properties)
    
    def create_input(self, variable, properties=None):
        """Create text input field"""
        if self.canvas is None:
            raise RuntimeError("Window must be created before adding widgets")
        
        properties = properties or {}
        theme = self.themes[self.theme]
        
        x = int(self.evaluate(properties.get('x', 100)))
        y = int(self.evaluate(properties.get('y', 100)))
        width = int(self.evaluate(properties.get('width', 200)))
        height = int(self.evaluate(properties.get('height', 30)))
        
        color = self.evaluate(properties.get('color', theme['input_fg']))
        bgcolor = self.evaluate(properties.get('bgcolor', theme['input_bg']))
        font_size = int(self.evaluate(properties.get('size', 12)))
        font_name = self.evaluate(properties.get('font', 'Arial'))
        
        # Create StringVar for the input
        var = tk.StringVar()
        self.input_vars[variable] = var
        
        # Create entry widget
        entry = tk.Entry(
            self.canvas,
            textvariable=var,
            bg=bgcolor,
            fg=color,
            font=(font_name, font_size),
            relief=tk.FLAT,
            borderwidth=2,
            insertbackground=color
        )
        
        entry_window = self.canvas.create_window(x, y, window=entry, anchor='nw', width=width, height=height)
        
        self.widgets.append({
            'type': 'input',
            'widget': entry,
            'window_id': entry_window,
            'variable': variable,
            'var': var
        })
        
        return entry
    
    def show_window(self):
        """Display the window and start main loop"""
        if self.window:
            self.window.update()
    
    def hide_window(self):
        """Hide the window"""
        if self.window:
            self.window.withdraw()
    
    def run_mainloop(self):
        """Start Tkinter main loop"""
        if self.root:
            self.root.mainloop()
    
    def get_input_value(self, variable):
        """Get value from input field"""
        if variable in self.input_vars:
            return self.input_vars[variable].get()
        return None
    
    def trigger_callback(self, callback_name):
        """Trigger a callback function - call StoryScript function or jump to label"""
        if callback_name in self.button_callbacks:
            # Custom Python callback
            self.button_callbacks[callback_name]()
        elif self.interpreter:
            # Try to call a StoryScript function
            if callback_name in self.interpreter.functions:
                func = self.interpreter.functions[callback_name]
                # Call the function with no arguments
                # DON'T apply closure for callbacks - we want them to access current global state
                # (applying closure would reset variables to their values when function was defined)
                try:
                    for stmt in func.body:
                        self.interpreter.execute(stmt)
                except Exception as e:
                    print(f"Error in callback '{callback_name}': {e}")
            # Try to jump to a label
            elif callback_name in self.interpreter.labels:
                self.interpreter.current_pos = self.interpreter.labels[callback_name]
                print(f"Button triggered: jumping to label '{callback_name}'")
            else:
                print(f"Warning: Callback '{callback_name}' not found (not a function or label)")
    
    def register_callback(self, name, function):
        """Register a custom Python callback function"""
        self.button_callbacks[name] = function
    
    def evaluate(self, value):
        """Evaluate a value (convert to appropriate type)"""
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            # Try to parse as number
            try:
                if '.' in value:
                    return float(value)
                return int(value)
            except ValueError:
                return value
        return value
    
    def clear_widgets(self):
        """Clear all widgets"""
        for widget_info in self.widgets:
            if 'widget' in widget_info:
                widget_info['widget'].destroy()
        self.widgets.clear()
    
    def update_textbox(self, widget_id, new_text):
        """Update the text of a textbox by ID"""
        if widget_id in self.named_widgets:
            widget_data = self.named_widgets[widget_id]
            if widget_data['type'] == 'textbox':
                widget_data['widget'].config(text=str(new_text))
            else:
                print(f"Warning: Widget '{widget_id}' is not a textbox")
        else:
            print(f"Warning: Widget ID '{widget_id}' not found")
    
    def destroy(self):
        """Destroy the GUI"""
        if self.root:
            self.root.destroy()
            self.root = None
            self.window = None
