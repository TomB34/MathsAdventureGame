import character as char
import pyinputplus as pyip
import random, time, datetime


def initEnemy(enemyStatsDict):
    enemyStatsDict['Health'] = random.randint(3, 5)

def initBoss(bossStatsDict):
    bossStatsDict['Health'] = random.randint(5, 7)


def combatChoices(userchoices):
    userchoices.append("Fight")


def askMathsQuestion(userHealth, enemyHealth):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    qStart = datetime.datetime.now()
    mathsQ = input(f"{x} x {y} = ")
    qEnd = datetime.datetime.now()
    qLenght = int(qEnd.strftime("%S")) - int(qStart.strftime("%S"))

    # Outcomes if user's answer is correct
    if mathsQ == str(x * y):
        if qLenght <= 2:
            print("Correct, a critical blow!")
            print("You deal the enemy 2 health points of damage!")
            enemyHealth -= 2
            print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")
            time.sleep(1)
        elif qLenght <= 5:
            print("Correct!")
            print("You deal the enemy 1 health point of damage!")
            enemyHealth -= 1
            print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")
            time.sleep(1)
        elif qLenght > 5:
            print("Correct, but the monster is too fast for your attack.")
            print("You deal the enemy 0 health points worth of damage!")
            print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")
            time.sleep(1)

    # Outcomes if user's answer is incorrect
    else:
        if qLenght <= 2:
            print("You attack too quickly with an incorrect answer!")
            print(f"The answer was {x * y}. You lose 2 health point")
            userHealth -= 2
            print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")
            time.sleep(1)
        else:
            print(f"Incorrect! The answer was {x * y}. You lose 1 health point")
            userHealth -= 1
            print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")
            time.sleep(1)

    return userHealth, enemyHealth


def enemyDrop(userInv, enemyCount):
    if enemyCount == 1 and userInv['Keys'] == 0:
        userInv['Keys'] = 1
        print('The enemy drops a key!')
    elif random.randint(0, 1) == 1 and userInv['Keys'] == 0:
        userInv['Keys'] = 1
        print('The enemy drops a key!')


def bossMathsQuestion(userHealth, bossHealth):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    op = random.randint(0, 1)

    qStart = datetime.datetime.now()
    if op == 0:
        mathsQ = f"{x} * {y} + {z}"
        mathsQAns = input(f"{x} x {y} + {z} = ")
    else:
        mathsQ = f"{x} * {y} - {z}"
        mathsQAns = input(f"{x} x {y} - {z} = ")
    qEnd = datetime.datetime.now()
    qLenght = int(qEnd.strftime("%S")) - int(qStart.strftime("%S"))

    # Outcomes if user's answer is correct
    if mathsQAns == str(eval(mathsQ)):
        if qLenght <= 2:
            print("Correct, a critical blow!")
            print("You deal the enemy 2 health points of damage!")
            bossHealth -= 2
            print(f"Your Health: {userHealth}, Enemy's Health: {bossHealth}\n")
            time.sleep(1)
        elif qLenght <= 5:
            print("Correct!")
            print("You deal the enemy 1 health point of damage!")
            bossHealth -= 1
            print(f"Your Health: {userHealth}, Enemy's Health: {bossHealth}\n")
            time.sleep(1)
        elif qLenght > 5:
            print("Correct, but the monster is too fast for your attack.")
            print("You deal the enemy 0 health points worth of damage!")
            print(f"Your Health: {userHealth}, Enemy's Health: {bossHealth}\n")
            time.sleep(1)

    # Answers if user's answer is incorrect
    else:
        if qLenght <= 2:
            print("You attack too quickly with an incorrect answer!")
            print(f"The answer was {str(eval(mathsQ))}. You lose 2 health point")
            userHealth -= 2
            print(f"Your Health: {userHealth}, Enemy's Health: {bossHealth}\n")
            time.sleep(1)
        else:
            print(f"Incorrect! The answer was {str(eval(mathsQ))}. You lose 1 health point")
            userHealth -= 1
            print(f"Your Health: {userHealth}, Enemy's Health: {bossHealth}\n")
            time.sleep(1)

    return userHealth, bossHealth

enemyStats = {
    'Health': 0
}

bossStats = {
    'Health': 0
}
