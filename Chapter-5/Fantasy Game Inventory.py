"""
Fantasy Game Inventory.
Displays and Game Inventory.
"""

# The inventory.
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    """Prints each key-value pair in the inventory."""
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)

# Calls the function, passing the inventory list as the argument.
displayInventory(stuff)
