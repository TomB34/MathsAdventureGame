#!python3
# textAdventureGame.py - My First Text Adventure Game

import mapGenerator as mapGen

#0 = empty coord, 1 = start room, 2 = empty room, 3 = enemy room, 4 = loot room, 5 = boss room

mapGen.printMap(mapGen.fullMap)

currentRoom = mapGen.startRoom
print(currentRoom)







