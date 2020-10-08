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


def doorChoices(doors):
    userChoices = []
    for i in range(4):
        if doors[i] != None and i == 0:
            userChoices.append('Go forward')
        if doors[i] != None and i == 1:
            userChoices.append('Go right')
        if doors[i] != None and i == 2:
            userChoices.append('Go backwards')
        if doors[i] != None and i == 3:
            userChoices.append('Go left')
    return userChoices