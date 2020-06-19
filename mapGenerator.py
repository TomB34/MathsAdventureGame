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


#Create array of random room types
#0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room
roomTypeList = [5]
for x in range(random.randint(12, 20)):
    roomTypeList.insert(0, random.randint(2, 4))

#Decide on room direction
#1 = N, 2 = E, 3 = S, 4 = W
roomDirection = 1

#Pick random room from coList for new room to adjoin to
adjRoom = coList[random.randint(0, len(coList) - 1)]
print("adjRoom: " + str(adjRoom))

#TODO: Check if adjoining room in directon is empty
if roomDirection == 1:
    emptyRoomFound = False
    while emptyRoomFound == False:
        if adjRoom[1] == 0:
            roomToCheck = [adjRoom[0], adjRoom[1] + 4]
        else:
            roomToCheck = [adjRoom[0], adjRoom[1] - 1]
        print("Room to check: " + str(roomToCheck))
        fullMap[roomToCheck[1]][roomToCheck[0]] = 2

    for y in range(5):
        print(fullMap[y])




