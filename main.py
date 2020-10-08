import pyinputplus as pyip
import sys, time

import directionChoices as dirCho
import roomDesc, enemyCombat

import user, chest, map


def defaultChoices(userChoicesList):
    userChoicesList.append('Check stats')
    userChoicesList.append('Check pockets')
    userChoicesList.append('Check map')
    userChoicesList.append('Quit')


# ------------------------------------------------------------------------------------------------

# Init objects
player = user.User()

# Set Current room, full map and user map
currentRoom = map.startRoom

# List of possible directions to go in from current room
doorList = dirCho.doorAmount(map.fullMap, currentRoom)

# List options for User
playing = True
isStart = True
while playing:

    # Prints a specific sentence when the game is started
    if isStart:
        print("You wake up in a damp and dimly lit room. A single flickering candle throws up shadows on the four grey stone walls.")
        isStart = False
        roomType = 1
    else:
        roomType = roomDesc.roomDesc(currentRoom, map.fullMap)

    # take current room and mapGen.fullMap. See what value fills current room and print appropriately
    userChoices = []
    # Start room, empty rooms and emptied chest rooms
    if roomType == 1 or roomType == 2 or roomType == 8:
        userChoices = dirCho.doorChoices(doorList)

    elif roomType == 3:  # Enemy room upon first entry
        enemyCombat.combatChoices(userChoices)
        enemyCombat.initEnemy(enemyCombat.enemyStats)
        map.fullMap[currentRoom[1]][currentRoom[0]] = 6
        print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")
    elif roomType == 6:  # Enemy room after first entry
        enemyCombat.combatChoices(userChoices)
        print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")
    elif roomType == 7:  # Defeated enemy room
        userChoices = dirCho.doorChoices(doorList)
    elif roomType == 4:  # Chest room
        userChoices = dirCho.doorChoices(doorList)
        userChoices.append('Open chest')
    elif roomType == 5:
        enemyCombat.combatChoices(userChoices)
        enemyCombat.initBoss(enemyCombat.bossStats)
        print(f"Boss Health: {enemyCombat.bossStats['Health']}")

    defaultChoices(userChoices)

    response = pyip.inputMenu(choices=userChoices, numbered=True)
    print()

    # TRAVEL FUNCTIONS
    if response == 'Go forward':
        # check for boss room
        if map.fullMap[doorList[0][1]][doorList[0][0]] == 5:
            if player.inventory['Keys'] == 0:
                print("The door is locked. Looks like it needs some sort of key")
                continue
            elif player.inventory['Keys'] == 1:
                print("The door requires a key. You try your one and it opens the door.")
                player.inventory['Keys'] = 0

        map.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[0][0], doorList[0][1]]
        map.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(map.fullMap, currentRoom)

    if response == 'Go right':
        # check for boss room
        if map.fullMap[doorList[1][1]][doorList[1][0]] == 5:
            if player.inventory['Keys'] == 0:
                print("The door is locked. Looks like it needs some sort of key")
                continue
            elif player.inventory['Keys'] == 1:
                print("The door requires a key. You try your one and it opens the door.")
                player.inventory['Keys'] = 0

        map.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[1][0], doorList[1][1]]
        map.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(map.fullMap, currentRoom)

    if response == 'Go backwards':
        # check for boss room
        if map.fullMap[doorList[2][1]][doorList[2][0]] == 5:
            if player.inventory['Keys'] == 0:
                print("The door is locked. Looks like it needs some sort of key")
                continue
            elif player.inventory['Keys'] == 1:
                print("The door requires a key. You try your one and it opens the door.")
                player.inventory['Keys'] = 0

        map.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[2][0], doorList[2][1]]
        map.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(map.fullMap, currentRoom)

    if response == 'Go left':
        # check for boss room
        if map.fullMap[doorList[3][1]][doorList[3][0]] == 5:
            if player.inventory['Keys'] == 0:
                print("The door is locked. Looks like it needs some sort of key")
                continue
            elif player.inventory['Keys'] == 1:
                print("The door requires a key. You try your one and it opens the door.")
                player.inventory['Keys'] = 0

        map.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[3][0], doorList[3][1]]
        map.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(map.fullMap, currentRoom)

    # CHEST ROOM FUNCTIONS
    if response == 'Open chest':
        chestItems = chest.openChest()
        player.stats['Health'] += chestItems[0]
        player.inventory['Gold Coins'] += chestItems[1]
        map.fullMap[currentRoom[1]][currentRoom[0]] = 8

    # ENEMY COMBAT FUNCTIONS
    if response == 'Fight':
        isFighting = True
        while isFighting:
            if roomType == 3:
                fightResult = enemyCombat.askMathsQuestion(player.stats['Health'], enemyCombat.enemyStats['Health'])

                if fightResult[0] <= 0:
                    print("You died, game over!")
                    sys.exit()
                if fightResult[1] <= 0:
                    print("You killed the creature!")
                    enemyCombat.enemyDrop(player.inventory, map.enemyCount)
                    map.enemyCount -= 1
                    map.fullMap[currentRoom[1]][currentRoom[0]] = 7
                    player.stats['Health'] = fightResult[0]
                    isFighting = False
                else:
                    player.stats['Health'] = fightResult[0]
                    enemyCombat.enemyStats['Health'] = fightResult[1]
            elif roomType == 5:
                fightResult = enemyCombat.bossMathsQuestion(player.stats['Health'], enemyCombat.bossStats['Health'])

                if fightResult[0] <= 0:
                    print("You died, game over!")
                    sys.exit()
                if fightResult[1] <= 0:
                    print("You defeated the final boss!")
                    print("Congratulations, you won the game!")
                    time.sleep(2)
                    sys.exit()
                else:
                    player.stats['Health'] = fightResult[0]
                    enemyCombat.bossStats['Health'] = fightResult[1]

    # DEFAULT FUNCTIONS
    if response == 'Check stats':
        for k, v in player.stats.items():
            print(f'{k}: {v}')

    if response == 'Check pockets':
        for k, v in player.inventory.items():
            print(f'{k}: {v}')

    if response == 'Check map':
        #mapGen.printMap(mapGen.userMap)
        map.printMap(map.fullMap)

    if response == 'Quit':
        sys.exit()
