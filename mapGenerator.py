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
print(coList)

for y in range(5):
    print(fullMap[y])

#TODO: Randomise room types and place them randomly in map

#0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room
roomTypeList = [5]
for x in range(random.randint(12, 20)):
    roomTypeList.append(random.randint(2, 4))

print(roomTypeList)


#add 10 randomly placed rooms that are all connected (Represented by '2')

#TODO: Turn adjRoom check into a function

for roomsToAdd in range(len(roomTypeList)):
    adjRoom = coList[random.randint(0, len(coList) - 1)] # Picks a random room from coList to have new room added to it
    roomType = roomTypeList.pop()

    if adjRoom == [0,0]:    # Checks if adjRoom is in a corner
        roomDirection = random.choice([2,3])
    elif adjRoom == [4,0]:
        roomDirection = random.choice([3,4])
    elif adjRoom == [4,4]:
        roomDirection = random.choice([1,4])
    elif adjRoom == [0, 4]:
        roomDirection = random.choice([1,3])

    elif adjRoom[1] == 0: # If room is at top edge, roomDirection cannot be '1' or 'North'
        roomDirection = random.choice([2,3,4])
    elif adjRoom[0] == 4: # If room is on right edge, roomDirection cannot be '2' or 'East'
        roomDirection = random.choice([1,3,4])
    elif adjRoom[1] == 4:
        roomDirection = random.choice([1,2,4])
    elif adjRoom[0] == 0:
        roomDirection = random.choice([1,2,3])
    else:
        roomDirection = random.choice([1,2,3,4])
    # print("adjRoom: " + str(adjRoom))
    # print("Room direction: " + str(roomDirection))

    #Check room to place coord is empty

    #TODO: Function that checks next coords along direction until empty coord is found
    isEmpty = False

    if roomDirection == 1:
        newRoom = [adjRoom[0], adjRoom[1] - 1]
        while isEmpty == False:
            if fullMap[newRoom[1]][newRoom[0]] == 0:
                print("Empty")
                fullMap[newRoom[1]][newRoom[0]] = roomType
    elif roomDirection == 2:
        newRoom = [adjRoom[0] + 1, adjRoom[1]]
        if fullMap[newRoom[1]][newRoom[0]] == 0:
            print("Empty")
            fullMap[newRoom[1]][newRoom[0]] = roomType
    elif roomDirection == 3:
        newRoom = [adjRoom[0], adjRoom[1] + 1]
        if fullMap[newRoom[1]][newRoom[0]] == 0:
            print("Empty")
            fullMap[newRoom[1]][newRoom[0]] = roomType
    elif roomDirection == 4:
        newRoom = [adjRoom[0] - 1, adjRoom[1]]
        if fullMap[newRoom[1]][newRoom[0]] == 0:
            print("Empty")
            fullMap[newRoom[1]][newRoom[0]] = roomType


    #Add new coord to coords list
    coList.append(newRoom)

for y in range(5):
    print(fullMap[y])

