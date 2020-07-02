import mapGenerator as mapGen
import pyinputplus as pyip
import sys

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

def printDoors(doors):
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

#TODO: Set Current room
currentRoom = mapGen.startRoom
fullMap = mapGen.fullMap
userMap = mapGen.userMap
print(currentRoom)

#TODO: Find out movement options for user
doorList = doorAmount(fullMap, currentRoom)
print(doorList)
mapGen.printMap(userMap)

#TODO: List options for User
playing = True
while playing:
    userChoices = printDoors(doorList)
    userChoices.append('Exit')
    response = pyip.inputMenu(choices=userChoices, numbered=True)
    if response == 'Go forward':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[0][0], doorList[0][1]]
        print(currentRoom)
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)
        mapGen.printMap(userMap)

    if response == 'Go right':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[1][0], doorList[1][1]]
        print(currentRoom)
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)
        mapGen.printMap(userMap)

    if response == 'Go back':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[2][0], doorList[2][1]]
        print(currentRoom)
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)
        mapGen.printMap(userMap)

    if response == 'Go left':
        userMap[currentRoom[1]][currentRoom[0]] = '-'
        currentRoom = [doorList[3][0], doorList[3][1]]
        print(currentRoom)
        userMap[currentRoom[1]][currentRoom[0]] = 'X'
        doorList = doorAmount(fullMap, currentRoom)
        mapGen.printMap(userMap)

    if response == 'Exit':
        sys.exit()


#TODO: Set current room to user-chosen room

#TODO: Put in loop to repeat













