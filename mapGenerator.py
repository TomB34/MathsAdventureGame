import random

#TODO: create a 5x5 map that randomly generates a sequence of connected rooms

#create a blank 5x5 2d array
fullMap = []
for y in range(5):
    fullMap.append([])
    for x in range(5):
        fullMap[y].append(0)

#Pick a random starting point (represented by '1')

coList = [] # List to store coords. Used to randomly pick from for room generations
coList.append([random.randint(0, 4), random.randint(0, 4)]) #Adds random square to list to serve as start room
fullMap[coList[0][1]][coList[0][0]] = 1 # Sets coords of first room to '1'
#print(coList)

for y in range(5):
    print(fullMap[y])


#Create array of random room types || 0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room
roomTypeList = []
for x in range(random.randint(5, 10)):
    roomTypeList.insert(0, random.randint(2, 4))


# Pick random room from coList for new room to adjoin to
for i in range(len(roomTypeList)):

    roomFound = False
    while roomFound == False:
        adjRoom = coList[random.randint(0, len(coList) - 1)]
        print("adjRoom: " + str(adjRoom))
        roomToCheck = []
        emptyRooms = []

        #TODO: check all directions for empty room. Add empty rooms to a list

        # Check North
        if adjRoom[1] == 0:
            roomToCheck = [adjRoom[0], adjRoom[1] + 4]
        else:
            roomToCheck = [adjRoom[0], adjRoom[1] - 1]

        if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:
            emptyRooms.append(roomToCheck)

        # Check East
        if adjRoom[0] == 4:
            roomToCheck = [adjRoom[0] - 4, adjRoom[1]]
        else:
            roomToCheck = [adjRoom[0] + 1, adjRoom[1]]
        if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:
            emptyRooms.append(roomToCheck)

        # Check South
        if adjRoom[1] == 4:
            roomToCheck = [adjRoom[0], adjRoom[1] - 4]
        else:
            roomToCheck = [adjRoom[0], adjRoom[1] + 1]
        if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:
            emptyRooms.append(roomToCheck)

        # Check West
        if adjRoom[0] == 0:
            roomToCheck = [adjRoom[0] + 4, adjRoom[1]]
        else:
            roomToCheck = [adjRoom[0] -1, adjRoom[1]]
        if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:
            emptyRooms.append(roomToCheck)

        # If no rooms are found, change adjRoom
        if emptyRooms == []:
            adjRoom = coList[random.randint(0, len(coList) - 1)]
        else:
            roomFound = True

            print("Empty rooms to pick from: " + str(emptyRooms))

            #TODO: pick a room at random to fill. Add to coList.
            roomToFill = random.choice(emptyRooms)
            coList.append(roomToFill)
            fullMap[roomToFill[1]][roomToFill[0]] = roomTypeList.pop()
            print("List of full rooms: " + str(coList) + "\n")

        for y in range(5):
            print(fullMap[y])




