import random


def openChest():
    # List of items that can be found in a chest
    possibleItems = ['Food', 'Gold Coins']

    # pick random number for amount of item types
    itemAmount = random.randint(1, 2)

    # pick random items from list
    loot = []
    for i in range(itemAmount):
        randIndex = random.randint(0, len(possibleItems) - 1)
        randItem = possibleItems.pop(randIndex)
        loot.append(randItem)

    # iterate through loot and add to stats or inventory
    foodAmount = 0
    coinAmount = 0
    for i in range(len(loot)):
        if loot[i] == 'Food':
            foodAmount += 1
            print('You find food! +1 Health')
        if loot[i] == 'Gold Coins':
            coinAmount = random.randint(1, 3)
            if coinAmount == 1:
                print("You find 1 Gold Coin!")
            else:
                print(f"You find {coinAmount} Gold Coins!")
    return foodAmount, coinAmount
