import random
import character as char

def openChest(inv, stats):
    #List of items that can be found in a chest
    possibleItems = ['Sword', 'Armour', 'Food', 'Gold Coins']

    #pick random number for amount of item types
    itemAmount = random.randint(1, 2)

    #pick random items from list
    loot = []
    for i in range(itemAmount):
        randIndex = random.randint(0, len(possibleItems) - 1)
        randItem = possibleItems.pop(randIndex)
        loot.append(randItem)

    #iterate through loot and add to stats or inventory
    for i in range(len(loot)):
        if loot[i] == 'Sword':
            char.charStats['Attack'] += 1
            print('You find a sword! +1 Attack!')
        if loot[i] == 'Armour':
            char.charStats['Defence'] += 1
            print('You find armour! +1 Defence!')
        if loot[i] == 'Food':
            char.charStats['Health'] += 1
            print('You find food! +1 Health')
        if loot[i] == 'Gold Coins':
            coinAmount = random.randint(1, 3)
            char.inventory['Gold Coins'] += coinAmount
            if coinAmount == 1:
                print("You find 1 Gold Coin!")
            else:
                print(f"You find {coinAmount} Gold Coins!")


