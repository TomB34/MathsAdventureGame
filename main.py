import pyinputplus as pyip
import sys
import time

import enemyCombat
import user
import chest
import map


def defaultChoices(userChoicesList):
    userChoicesList.append('Check stats')
    userChoicesList.append('Check pockets')
    userChoicesList.append('Check map')
    userChoicesList.append('Quit')


# ------------------------------------------------------------------------------------------------

# Init user stats
player = user.User()

# Set Current room, full map and user map
currentRoom = map.startRoom

# List of possible directions to go in from current room
doorList = map.doorAmount(map.fullMap, currentRoom)

playing = True
isStart = True
while playing:

    # Prints a specific sentence when the game is started
    if isStart:
        print("You wake up in a damp and dimly lit room. A single flickering candle throws up shadows on the four "
              "grey stone walls.")
        isStart = False
        roomType = 1
    else:
        roomType = map.roomDesc(currentRoom, map.fullMap)

    # USER CHOICES SECTION
    userChoices = []
    # Start room, empty rooms and emptied chest rooms
    if roomType == 1 or roomType == 2 or roomType == 8:
        userChoices = map.doorChoices(doorList)
    # Enemy room upon first entry
    elif roomType == 3:
        enemyCombat.combatChoices(userChoices)
        enemyCombat.initEnemy(enemyCombat.enemyStats)
        map.fullMap[currentRoom[1]][currentRoom[0]] = 6
        print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")
    # Enemy room after first entry
    elif roomType == 6:
        enemyCombat.combatChoices(userChoices)
        print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")
    # Defeated enemy room
    elif roomType == 7:
        userChoices = map.doorChoices(doorList)
    # Chest room
    elif roomType == 4:
        userChoices = map.doorChoices(doorList)
        userChoices.append('Open chest')
    # Boss room
    elif roomType == 5:
        enemyCombat.combatChoices(userChoices)
        enemyCombat.initBoss(enemyCombat.bossStats)
        print(f"Boss Health: {enemyCombat.bossStats['Health']}")
    defaultChoices(userChoices)

    # USERS INPUT
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
        doorList = map.doorAmount(map.fullMap, currentRoom)

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
        doorList = map.doorAmount(map.fullMap, currentRoom)

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
        doorList = map.doorAmount(map.fullMap, currentRoom)

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
        doorList = map.doorAmount(map.fullMap, currentRoom)

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
        map.printMap(map.userMap)
        # Uncomment to be able to view full map in game
        # map.printMap(map.fullMap)

    if response == 'Quit':
        sys.exit()