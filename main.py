import mapGenerator as mapGen
import pyinputplus as pyip
import sys, roomDesc

def doorAmount(fullMap, currentRoom):
    doors = []
    if currentRoom[1] == 0:
        roomToCheck = [currentRoom[0], currentRoom[1] + 4]
    else:
        roomToCheck = [currentRoom[0], currentRoom[1] - 1]
    if fullMap[roomToCheck[1]][roomToCheck[0]] != 0:
        doors.append(roomToCheck)
    else:
        doors.append(None)

    if currentRoom[0] == 4:
        roomToCheck = [currentRoom[0] - 4, currentRoom[1]]
    else:
        roomToCheck = [currentRoom[0] + 1, currentRoom[1]]
    if fullMap[roomToCheck[1]][roomToCheck[0]] != 0:
        doors.append(roomToCheck)
    else:
        doors.append(None)

    if currentRoom[1] == 4:
        roomToCheck = [currentRoom[0], currentRoom[1] - 4]
    else:
        roomToCheck = [currentRoom[0], currentRoom[1] + 1]
    if fullMap[roomToCheck[1]][roomToCheck[0]] != 0:
        doors.append(roomToCheck)
    else:
        doors.append(None)

    if currentRoom[0] == 0:
        roomToCheck = [currentRoom[0] + 4, currentRoom[1]]
    else:
        roomToCheck = [currentRoom[0] - 1, currentRoom[1]]
    if fullMap[roomToCheck[1]][roomToCheck[0]] != 0:
        doors.append(roomToCheck)
    else:
        doors.append(None)

    return doors

def doorChoices(doors):
    userChoices = []
    for i in range(4):
        if doors[i] != None and i == 0:
            userChoices.append('Go forward')
        if doors[i] != None and i == 1:
            userChoices.append('Go right')
        if doors[i] != None and i == 2:
            userChoices.append('Go back')
        if doors[i] != None and i == 3:
            userChoices.append('Go left')
    return userChoices

def defaultChoices(userChoicesList):
    userChoicesList.append('Inventory')
    userChoicesList.append('Check map')
    userChoicesList.append('Quit')



#------------------------------------------------------------------------------------------------

#Set Current room
currentRoom = mapGen.startRoom
fullMap = mapGen.fullMap
userMap = mapGen.userMap

#Find out movement options for user
doorList = doorAmount(fullMap, currentRoom)

#Player's Inventory
inventory = {'Dagger/s': 1, 'Gold Coin/s': 3, 'key/s': 1}

#TODO: List options for User
playing = True
isStart = True
while playing:

    # Prints a description of the room
    if isStart == True:
        print("You wake up in a damp and dimly lit room. A single flickering candle throws up shadows on the four grey stone walls.")
        isStart = False
        roomType = 1
    else:
        roomType = roomDesc.roomDesc(currentRoom, mapGen.fullMap)
        print(roomType)
    #take current room and mapGen.fullMap. See what value fills current room and print appropriately

    if roomType == 1 or roomType == 2 or roomType == 4:
        userChoices = doorChoices(doorList)
    elif roomType == 3:
        userChoices = doorChoices(doorList)
    elif roomType == 5:
        userChoices = doorChoices(doorList)

    defaultChoices(userChoices)

    prompt = 'What would you like to do?\n'
    for i in range(len(userChoices)):
        prompt += f'{str(i + 1)}. {userChoices[i]}\n'

    response = pyip.inputMenu(choices=userChoices, numbered=True, prompt=prompt)

    if response == 'Go forward':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[0][0], doorList[0][1]]
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)

    if response == 'Go right':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[1][0], doorList[1][1]]
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)

    if response == 'Go back':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[2][0], doorList[2][1]]
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)

    if response == 'Go left':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[3][0], doorList[3][1]]
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)

    if response == 'Inventory':
        for k, v in enumerate(inventory):
            print(f'{v}: {k}')

    if response == 'Check map':
        mapGen.printMap(userMap)

    if response == 'Quit':
        sys.exit()
















