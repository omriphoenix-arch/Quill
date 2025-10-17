"""
Game Module for Quill
Game development utilities
"""

def get_game_functions(interpreter):
    """
    Return dictionary of game development functions
    
    Requires interpreter instance for inventory, save/load, and timing
    """
    import time
    import json
    import os
    
    # Timing Functions
    def wait(seconds):
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
    def add_item(item):
        """Add an item to the inventory"""
        item_name = str(item)
        interpreter.inventory.append(item_name)
        print(f"✓ Added '{item_name}' to inventory")
        return True
    
    def remove_item(item):
        """Remove an item from the inventory"""
        item_name = str(item)
        if item_name in interpreter.inventory:
            interpreter.inventory.remove(item_name)
            print(f"✓ Removed '{item_name}' from inventory")
            return True
        else:
            print(f"✗ '{item_name}' not found in inventory")
            return False
    
    def has_item(item):
        """Check if inventory contains an item"""
        item_name = str(item)
        return item_name in interpreter.inventory
    
    def show_inventory():
        """Display the inventory"""
        print("\n" + "="*40)
        print("          INVENTORY")
        print("="*40)
        
        if not interpreter.inventory:
            print("  (Empty)")
        else:
            # Count duplicate items
            item_counts = {}
            for item in interpreter.inventory:
                item_counts[item] = item_counts.get(item, 0) + 1
            
            # Display items
            for item, count in item_counts.items():
                if count > 1:
                    print(f"  • {item} (x{count})")
                else:
                    print(f"  • {item}")
        
        print("="*40)
        print(f"Total items: {len(interpreter.inventory)}")
        print("="*40 + "\n")
        return None
    
    def clear_inventory():
        """Clear all items from inventory"""
        interpreter.inventory.clear()
        print("✓ Inventory cleared")
        return True
    
    def item_count():
        """Get total number of items in inventory"""
        return len(interpreter.inventory)
    
    # Save/Load System Methods
    def save_game(filename):
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
                'inventory': interpreter.inventory.copy()
            }
            
            # Save only serializable variables
            for key, value in interpreter.variables.items():
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
    
    def load_game(filename):
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
            interpreter.variables.update(save_data.get('variables', {}))
            
            # Restore inventory
            interpreter.inventory = save_data.get('inventory', [])
            
            print(f"✓ Game loaded from: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading game: {e}")
            return False
    
    def has_save(filename):
        """Check if a save file exists"""
        # Ensure .save extension
        if not str(filename).endswith('.save'):
            filename = str(filename) + '.save'
        
        filepath = os.path.join('saves', filename)
        return os.path.exists(filepath)
    
    def delete_save(filename):
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
    
    return {
        # Timing
        'wait': wait,
        # Inventory
        'add_item': add_item,
        'remove_item': remove_item,
        'has_item': has_item,
        'show_inventory': show_inventory,
        'clear_inventory': clear_inventory,
        'item_count': item_count,
        # Save/Load
        'save_game': save_game,
        'load_game': load_game,
        'has_save': has_save,
        'delete_save': delete_save,
    }
