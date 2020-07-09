import pyinputplus as pyip
import sys

import mapGenerator as mapGen
import directionChoices as dirCho
import character as char
import roomDesc, chestFuncs, enemyCombat

def defaultChoices(userChoicesList):
    userChoicesList.append('Check stats')
    userChoicesList.append('Check pockets')
    userChoicesList.append('Check map')
    userChoicesList.append('Quit')

#------------------------------------------------------------------------------------------------

#Set Current room, full map and user map
currentRoom = mapGen.startRoom

#List of possible directions to go in from current room
doorList = dirCho.doorAmount(mapGen.fullMap, currentRoom)

#TODO: List options for User
playing = True
isStart = True
while playing:

    # Prints a specific sentence when the game is started
    if isStart == True:
        print("You wake up in a damp and dimly lit room. A single flickering candle throws up shadows on the four grey stone walls.")
        isStart = False
        roomType = 1
    else:
        roomType = roomDesc.roomDesc(currentRoom, mapGen.fullMap)

    #take current room and mapGen.fullMap. See what value fills current room and print appropriately
    userChoices = []
    if roomType == 1 or roomType == 2 or roomType == 8:
        userChoices = dirCho.doorChoices(doorList)

    elif roomType == 3: #Enemy room upon first entry
        enemyCombat.combatChoices(userChoices)
        enemyCombat.initEnemy(enemyCombat.enemyStats)
        mapGen.fullMap[currentRoom[1]][currentRoom[0]] = 6
        print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")
    elif roomType == 6: #Enemy room after first entry
        enemyCombat.combatChoices(userChoices)
        print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")
    elif roomType == 7: # Defeated enemy room
        userChoices = dirCho.doorChoices(doorList)
    elif roomType == 4: #Chest room
        userChoices = dirCho.doorChoices(doorList)
        userChoices.append('Open chest')
    elif roomType == 5:
        userChoices = dirCho.doorChoices(doorList)


    defaultChoices(userChoices)

    prompt = 'What would you like to do?\n'
    for i in range(len(userChoices)):
        prompt += f'{str(i + 1)}. {userChoices[i]}\n'

    response = pyip.inputMenu(choices=userChoices, numbered=True, prompt=prompt)

    # Travel functions
    if response == 'Go forward':
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[0][0], doorList[0][1]]
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(mapGen.fullMap, currentRoom)

    if response == 'Go right':
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[1][0], doorList[1][1]]
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(mapGen.fullMap, currentRoom)

    if response == 'Go back':
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[2][0], doorList[2][1]]
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(mapGen.fullMap, currentRoom)

    if response == 'Go left':
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[3][0], doorList[3][1]]
        mapGen.userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = dirCho.doorAmount(mapGen.fullMap, currentRoom)

    # Chest room functions
    if response == 'Open chest':
        chestFuncs.openChest(char.inventory, char.charStats)
        mapGen.fullMap[currentRoom[1]][currentRoom[0]] = 8

    # Enemy combat functions
    if response == 'Stab':
        stabResults = enemyCombat.userStab(char.charStats['Health'], char.charStats['Attack'], enemyCombat.enemyStats['Health'], enemyCombat.enemyStats['Defence'])
        if stabResults[0] <= 0:
            print('You died, game over!')
            sys.exit()
        if stabResults[1] <= 0:
            print('You killed the creature!')
            mapGen.fullMap[currentRoom[1]][currentRoom[0]] = 7
            char.charStats['Health'] = stabResults[0]
        else:
            char.charStats['Health'] = stabResults[0]
            enemyCombat.enemyStats['Health'] = stabResults[1]
            print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")

    if response == 'Swipe':
        swipeResults = enemyCombat.userSwipe(char.charStats['Health'], char.charStats['Attack'], enemyCombat.enemyStats['Health'], enemyCombat.enemyStats['Defence'])
        if swipeResults[0] <= 0:
            print('You died, game over!')
            sys.exit()
        if swipeResults[1] <= 0:
            print('You killed the creature!')
            mapGen.fullMap[currentRoom[1]][currentRoom[0]] = 7
            char.charStats['Health'] = swipeResults[0]
        else:
            char.charStats['Health'] = swipeResults[0]
            enemyCombat.enemyStats['Health'] = swipeResults[1]
            print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")

    if response == 'Block':
        blockResults = enemyCombat.userBlock(char.charStats['Health'], char.charStats['Defence'], enemyCombat.enemyStats['Attack'])
        if blockResults <= 0:
            print('You died, game over!')
            sys.exit()
        else:
            char.charStats['Health'] = blockResults
            print(f"Enemy Health: {enemyCombat.enemyStats['Health']}")

    # Default functions
    if response == 'Check stats':
        for k, v in char.charStats.items():
            print(f'{k}: {v}')

    if response == 'Check pockets':
        for k, v in char.inventory.items():
            print(f'{k}: {v}')

    if response == 'Check map':
        mapGen.printMap(mapGen.userMap)

    if response == 'Quit':
        sys.exit()
















