import random

def checkSides(fullMapList, adjRoomCoords):   #Takes full map, adjRoom coords
    emptyRooms = []
    # Check North
    if adjRoomCoords[1] == 0:
        roomToCheck = [adjRoomCoords[0], adjRoomCoords[1] + 4]
    else:
        roomToCheck = [adjRoomCoords[0], adjRoomCoords[1] - 1]

    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    # Check East
    if adjRoomCoords[0] == 4:
        roomToCheck = [adjRoomCoords[0] - 4, adjRoomCoords[1]]
    else:
        roomToCheck = [adjRoomCoords[0] + 1, adjRoomCoords[1]]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    # Check South
    if adjRoomCoords[1] == 4:
        roomToCheck = [adjRoomCoords[0], adjRoomCoords[1] - 4]
    else:
        roomToCheck = [adjRoomCoords[0], adjRoomCoords[1] + 1]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    # Check West
    if adjRoomCoords[0] == 0:
        roomToCheck = [adjRoomCoords[0] + 4, adjRoomCoords[1]]
    else:
        roomToCheck = [adjRoomCoords[0] - 1, adjRoomCoords[1]]
    if fullMapList[roomToCheck[1]][roomToCheck[0]] == 0:
        emptyRooms.append(roomToCheck)

    return emptyRooms
    # Returns a list of empty rooms that are available to be used

def printMap(fullMaplist):
    print("X is the room you are in. - are rooms you have been in. 0 are undiscovered places.")
    for y in range(5):
        for x in range(5):
            print(str(fullMaplist[y][x]) + " ", end='')
        print()

#create a blank 5x5 2d array
fullMap = []
userMap = []
for y in range(5):
    fullMap.append([])
    userMap.append([])
    for x in range(5):
        fullMap[y].append(0)
        userMap[y].append(0)

#Pick a random starting point (represented by '1')

# List to store coords. Used to randomly pick from for room generations
coList = []
#Startroom represented by '1' to be the spawn room
startRoom = [random.randint(0, 4), random.randint(0, 4)]
coList.append(startRoom)
fullMap[coList[0][1]][coList[0][0]] = 1
userMap[coList[0][1]][coList[0][0]] = 'X'

#Create array of random room types
# 0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room
roomTypeList = [3, 4]
for x in range(random.randint(5, 7)):
    roomTypeList.append(random.randint(2, 4))

# Pick random room from coList for new room to adjoin to
for i in range(len(roomTypeList)):
    roomFound = False
    while roomFound == False:
        adjRoom = coList[random.randint(0, len(coList) - 1)]
        roomToCheck = []

        emptyRooms = checkSides(fullMap, adjRoom)

        # If no rooms are found, change adjRoom
        if emptyRooms == []:
            adjRoom = coList[random.randint(0, len(coList) - 1)]
        else:
                roomFound = True    #Breaks from while loop, allows for next room to be made
                #pick a room at random to from the list to fill. Add to coList.
                roomToFill = random.choice(emptyRooms)
                coList.append(roomToFill)
                fullMap[roomToFill[1]][roomToFill[0]] = roomTypeList.pop()
                #print("List of full rooms: " + str(coList) + "\n")

#Add boss room, not adjacent to start room
bossRoomFound = False
while bossRoomFound == False:
    adjRoom = coList[random.randint(1, len(coList) - 1)]    #Start at index 1 to miss out start room
    roomToCheck = []

    emptyRooms = checkSides(fullMap, adjRoom)

    if emptyRooms == []:
        adjRoom = coList[random.randint(1, len(coList) - 1)]
    else:
        bossRoomFound = True
        roomToFill = random.choice(emptyRooms)
        coList.append(roomToFill)
        fullMap[roomToFill[1]][roomToFill[0]] = 5




