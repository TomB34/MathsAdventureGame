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


#Create array of random room types
#0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room
roomTypeList = [5]
for x in range(random.randint(12, 20)):
    roomTypeList.insert(0, random.randint(2, 4))



#TODO: Check if adjoining room in directon is empty
for rooms in range(5):
    # Decide on room direction
    # 1 = N, 2 = E, 3 = S, 4 = W
    roomDirection = random.randint(1, 4)

    # Pick random room from coList for new room to adjoin to
    adjRoom = coList[random.randint(0, len(coList) - 1)]
    print("adjRoom: " + str(adjRoom))


    if roomDirection == 1:  #If direction is north
        emptyRoomFound = False  #Set to False

        if adjRoom[1] == 0: #If Y coordinate is 0 - At the top of map
            roomToCheck = [adjRoom[0], adjRoom[1] + 4]  #Mirror new room to bottom of map
        else:
            roomToCheck = [adjRoom[0], adjRoom[1] - 1]  #Otherwise go up one for new room
        print("Room to check!!!: " + str(roomToCheck))

        #While loop will check for new empty room if first room doesn't work
        while emptyRoomFound == False:  #While empty room hasn't been found
            if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:    #If roomToCheck coords are empty
                fullMap[roomToCheck[1]][roomToCheck[0]] = 2     #Set room to value of 2
                emptyRoomFound = True   #Empty room found, set to True
                print("Empty room found!")
            elif fullMap[roomToCheck[1]][roomToCheck[0]] != 0:  #If roomToCheck is taken
                if roomToCheck[1] == 0: #If room that was checked is on top edge...
                    roomToCheck = [roomToCheck[0], roomToCheck[1] + 4]  #Mirror new roomToCheck
                    print("Room to check?: " + str(roomToCheck))
                elif roomToCheck[1] != 0:
                    roomToCheck = [roomToCheck[0], roomToCheck[1] - 1]  #Otherwise move new roomToCheck up
                    print("Room to check!: " + str(roomToCheck))

    if roomDirection == 2:
        emptyRoomFound = False  # Set to False

        if adjRoom[0] == 4:  # If X coordinate is 4 - Right edge of map
            roomToCheck = [adjRoom[0] - 4, adjRoom[1]]  # Mirror new room to left of map
        else:
            roomToCheck = [adjRoom[0] + 1, adjRoom[1]]  # Otherwise go right one for new room
        print("Room to check!!!: " + str(roomToCheck))

        # While loop will check for new empty room if first room is full
        while emptyRoomFound == False:  # While empty room hasn't been found
            if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:  # If roomToCheck coords are empty
                fullMap[roomToCheck[1]][roomToCheck[0]] = 2  # Set room to value of 2
                emptyRoomFound = True  # Empty room found, set to True
                print("Empty room found!")
            elif fullMap[roomToCheck[1]][roomToCheck[0]] != 0:  # If roomToCheck is taken
                if roomToCheck[0] == 4:  # If room that was checked is on right edge...
                    roomToCheck = [roomToCheck[0] - 4, roomToCheck[1]]  # Mirror new roomToCheck
                    print("Room to check?: " + str(roomToCheck))
                elif roomToCheck[0] != 4:
                    roomToCheck = [roomToCheck[0] + 1, roomToCheck[1]]  # Otherwise move new roomToCheck to right
                    print("Room to check!: " + str(roomToCheck))

    if roomDirection == 3:
        emptyRoomFound = False  # Set to False

        if adjRoom[1] == 4:  # If Y coordinate is 4 - At the bottom of map
            roomToCheck = [adjRoom[0], adjRoom[1] - 4]  # Mirror new room to top of map
        else:
            roomToCheck = [adjRoom[0], adjRoom[1] + 1]  # Otherwise go down one for new room
        print("Room to check!!!: " + str(roomToCheck))

        # While loop will check for new empty room if first room doesn't work
        while emptyRoomFound == False:  # While empty room hasn't been found
            if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:  # If roomToCheck coords are empty
                fullMap[roomToCheck[1]][roomToCheck[0]] = 2  # Set room to value of 2
                emptyRoomFound = True  # Empty room found, set to True
                print("Empty room found!")
            elif fullMap[roomToCheck[1]][roomToCheck[0]] != 0:  # If roomToCheck is taken
                if roomToCheck[1] == 4:  # If room that was checked is on bottom edge...
                    roomToCheck = [roomToCheck[0], roomToCheck[1] - 4]  # Mirror new roomToCheck
                    print("Room to check?: " + str(roomToCheck))
                elif roomToCheck[1] != 4:
                    roomToCheck = [roomToCheck[0], roomToCheck[1] + 1]  # Otherwise move new roomToCheck down
                    print("Room to check!: " + str(roomToCheck))

    if roomDirection == 4:
        emptyRoomFound = False  # Set to False

        if adjRoom[0] == 0:  # If X coordinate is 0 - Left edge of map
            roomToCheck = [adjRoom[0] + 4, adjRoom[1]]  # Mirror new room to right of map
        else:
            roomToCheck = [adjRoom[0] - 1, adjRoom[1]]  # Otherwise go left one for new room
        print("Room to check!!!: " + str(roomToCheck))

        # While loop will check for new empty room if first room is full
        while emptyRoomFound == False:  # While empty room hasn't been found
            if fullMap[roomToCheck[1]][roomToCheck[0]] == 0:  # If roomToCheck coords are empty
                fullMap[roomToCheck[1]][roomToCheck[0]] = 2  # Set room to value of 2
                emptyRoomFound = True  # Empty room found, set to True
                print("Empty room found!")
            elif fullMap[roomToCheck[1]][roomToCheck[0]] != 0:  # If roomToCheck is taken
                if roomToCheck[0] == 0:  # If room that was checked is on left edge...
                    roomToCheck = [roomToCheck[0] + 4, roomToCheck[1]]  # Mirror new roomToCheck
                    print("Room to check?: " + str(roomToCheck))
                elif roomToCheck[0] != 4:
                    roomToCheck = [roomToCheck[0] - 1, roomToCheck[1]]  # Otherwise move new roomToCheck to left
                    print("Room to check!: " + str(roomToCheck))


for y in range(5):
    print(fullMap[y])




