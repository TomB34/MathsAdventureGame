import pyinputplus as pyip
import sys

import mapGenerator as mapGen
import directionChoices as dirCho
import character as char
import roomDesc, chestFuncs

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

    if roomType == 1 or roomType == 2 or roomType == 8:
        userChoices = dirCho.doorChoices(doorList)
    elif roomType == 3:
        userChoices = dirCho.doorChoices(doorList)
    elif roomType == 4:
        userChoices = dirCho.doorChoices(doorList)
        userChoices.append('Open chest')
    elif roomType == 5:
        userChoices = dirCho.doorChoices(doorList)

    defaultChoices(userChoices)

    prompt = 'What would you like to do?\n'
    for i in range(len(userChoices)):
        prompt += f'{str(i + 1)}. {userChoices[i]}\n'

    response = pyip.inputMenu(choices=userChoices, numbered=True, prompt=prompt)

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

    if response == 'Open chest':
        chestFuncs.openChest(char.inventory, char.charStats)
        mapGen.fullMap[currentRoom[1]][currentRoom[0]] = 8

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
















