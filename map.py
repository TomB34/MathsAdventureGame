import random


# Prints map
def printMap(mapList):
    print("X is the room you are in. - are rooms you have been in. 0 are undiscovered places.")
    for y in range(5):
        for x in range(5):
            print(str(mapList[y][x]) + " ", end='')
        print()


# Initialises 5x5 array filled with 0s
def initEmptyMap(mapList):
    # Create a blank 5x5 2d array
    for y in range(5):
        mapList.append([])
        for x in range(5):
            mapList[y].append(0)


# Initialises the room that a user begins in
def initStartRoom(fullMapList, userMapList, coList):
    startRoom = [random.randint(0, 4), random.randint(0, 4)]
    coList.append(startRoom)
    fullMapList[coList[0][1]][coList[0][0]] = 1
    userMapList[coList[0][1]][coList[0][0]] = 'X'
    return startRoom


# Returns a list of random room types along with an enemy count
def generateRooms():
    roomTypesList = [3, 4, 3]
    enCount = 2
    for i in range(random.randint(5, 7)):
        rndRoom = random.randint(2, 4)
        roomTypesList.append(rndRoom)
        if rndRoom == 3:
            enCount += 1
    return roomTypesList, enCount


# Checks the sides of a room to see which sides are empty
def checkRoomSides(fullMapList, roomCoords):
    emptyRooms = []
    # HAVE CODE NOT REPEAT ITSELF
    # Check North
    if roomCoords[1] == 0:
        roomToCheck = [roomCoords[0], roomCoords[1] + 4]
    else:
        roomToCheck = [roomCoords[0], roomCoords[1] - 1]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    # Check East
    if roomCoords[0] == 4:
        roomToCheck = [roomCoords[0] - 4, roomCoords[1]]
    else:
        roomToCheck = [roomCoords[0] + 1, roomCoords[1]]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    # Check South
    if roomCoords[1] == 4:
        roomToCheck = [roomCoords[0], roomCoords[1] - 4]
    else:
        roomToCheck = [roomCoords[0], roomCoords[1] + 1]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    # Check West
    if roomCoords[0] == 0:
        roomToCheck = [roomCoords[0] + 4, roomCoords[1]]
    else:
        roomToCheck = [roomCoords[0] - 1, roomCoords[1]]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    return emptyRooms
    # Returns a list of empty rooms that are available to be used


def createMap(roomTypesList, coList, fullMapList):
    for i in range(len(roomTypesList)):
        roomFound = False
        # While an adjoining room hasn't yet been found
        while not roomFound:
            room = coList[random.randint(0, len(coList) - 1)]
            emptyRooms = checkRoomSides(fullMapList, room)

            # If all rooms around a room are taken, pick a new room at random
            if not emptyRooms:
                room = coList[random.randint(0, len(coList) - 1)]
            # If one or more empty rooms have been found
            else:
                roomFound = True
                # Pick a random room to assign a room type
                coordsToFill = random.choice(emptyRooms)
                # Add room to colist
                coList.append(coordsToFill)
                # Full map at coords of found room assigned room type var
                fullMapList[coordsToFill[1]][coordsToFill[0]] = roomTypesList.pop()


def initBossRoom(coList, fullMapList):
    bossRoomFound = False
    while not bossRoomFound:
        # Start at index of 1 to miss start room
        room = coList[random.randint(1, len(coList) - 1)]
        emptyRooms = checkRoomSides(fullMapList, room)

        if not emptyRooms:
            room = coList[random.randint(1, len(coList) - 1)]
        else:
            bossRoomFound = True
            coordsToFill = random.choice(emptyRooms)
            coordList.append(coordsToFill)
            fullMapList[coordsToFill[1]][coordsToFill[0]] = 5


# ----------------------------------------------------------------------------------------------------------------------
fullMap = []
userMap = []
coordList = []
adjacentRoom = []

# Create empty maps
initEmptyMap(fullMap)
initEmptyMap(userMap)

# Initialise a starting room
startRoom = initStartRoom(fullMap, userMap, coordList)

# Create a list of random room types
roomTypes, enemyCount = generateRooms()

# Create a map made from random room types
createMap(roomTypes, coordList, fullMap)
initBossRoom(coordList, fullMap)







