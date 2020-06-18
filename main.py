#!python3
# textAdventureGame.py - My First Text Adventure Game

import random



#TODO: Ask for Users Name
#print("Welcome to my text adventure game!")
#userName = input("Please enter your name to begin playing: ")



#TODO: Create rooms to travel to
#Use 2d array to randomise rooms
#Use different numbers within array to represent types of rooms and what characters go in them
#0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room


fullMap = []    # List will contain a 5x5 map
coordsList = [] # A list of lists that contains coord pairs

coordsList.append([0, 0])   #0,0 is beginner room

fullMap.append([1])   # Set start room to '1'

#Randomise total rooms, run through for loop and incremet emptyRoom variables randomly
emptyRoomNo = 0
enemyRoomNo = 1
lootRoomNo = 1
bossRoomNo = 1
totalRoomNo = 4 #random.randint(6, 12)

for rooms in range(totalRoomNo):
    roomType = random.randint(2, 4)
    if roomType == 2:
        emptyRoomNo += 1
    elif roomType == 3:
        enemyRoomNo += 1
    elif roomType == 4:
        lootRoomNo += 1

print("Empty rooms: " + str(emptyRoomNo))
print("Enemy rooms: " + str(enemyRoomNo))
print("Loot rooms: " + str(lootRoomNo))
print("Boss rooms: " + str(bossRoomNo) + "\n")

#TODO: add rooms to full map
# Make sure that rooms are connected
# Boss room must be placed last and can have only one doorway
# randomise which type of room is placed. Minus 1 from roomNo variable when used. If roomNo variable is 0 then don't add

#Pick random side of start room. Random number between one and four which correlate to NSEW. If room on edge lower options
#for rooms in range(totalRoomNo):


#print(roomDirection)



for roomsToAdd in range(totalRoomNo):
    newRoomX = 0    # Coords for new room
    newRoomY = 0
    adjRoomXY = coordsList[random.randint(0, len(coordsList) - 1)]  # picks random room from coordsList
    roomDirection = random.randint(1, 3)  # 1 = North, 2 = East, 3 = South, 4 = West
    print("Room Direction: " + str(roomDirection))
    print("adjRoomXY: " + str(adjRoomXY))

    if roomDirection == 1:
        fullMap.insert(0, [2])
        coordsList.append([adjRoomXY[0], adjRoomXY[1] + 1])
    if roomDirection == 2:
        fullMap[0].append(2)
        coordsList.append([adjRoomXY[0] + 1, adjRoomXY[1]])
    if roomDirection == 3:
        fullMap.append([2])
        coordsList.append([adjRoomXY[0], adjRoomXY[1] - 1 ])
    if roomDirection == 4:
        fullMap[0].insert(0, 2)
        coordsList.append([adjRoomXY[0] - 1, adjRoomXY[1]])



for x in range(len(fullMap)):
    print(fullMap[x])





