"""
List to Dictionary Function for Fantasy Game Inventory.
"""

def addToInventory(inventory, addedItems):
    """Loops through loot, adds to inventory."""
    numberAdded = 0
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return 1

def displayInventory(inventory):
    """Function to display inventory."""
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)

inv = {'gold coin': 42, 'rope': 1} # original inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] # LOOT!
inv2 = addToInventory(inv, dragonLoot) # passes current inventory and loot
# as arguments
displayInventory(inv) # calls function to display inventory
