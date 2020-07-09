import random, enemyCombat

def roomDesc (currentRoom, fullMap):
    roomType = fullMap[currentRoom[1]][currentRoom[0]]
    if roomType == 1:
        print("You find yourself in the room that you woke up in")
    if roomType == 2:
        emptyRoomLines = ["An empty room, not much to see here",
                          "Not much to look at here",
                          "Nothing exciting here"]
        print(emptyRoomLines[random.randint(0, len(emptyRoomLines) - 1)])
    if roomType == 3 or roomType == 6:
        print(f"A creature stands before you, preventing you from getting out.")
        #Call enemy fight function here in new module
    if roomType == 7:
        print("A slain foe lays in the middle of the room.")
    if roomType == 4:
        print("A chest sits in the middle of the room")
        #Call loot function here
    if roomType == 5:
        print("A huge three-eyed monster stands before you, looking a lot tougher and hungrier than the previous foes you have faced")
        #Call boss function here
    if roomType == 8:
        print("An opened and empty chest sits in the middle of the room")

    return roomType



