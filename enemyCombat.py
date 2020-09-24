import character as char
import pyinputplus as pyip
import random


def initEnemy(enemyStatsDict):
    enemyStatsDict['Health'] = random.randint(3, 5)


def combatChoices(userchoices):
    userchoices.append("Fight")


def askMathsQuestion(userHealth, enemyHealth):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    mathsPrompt = f"{x} x {y} = "
    mathsResp = pyip.inputInt(prompt=mathsPrompt)

    if mathsResp == x * y:
        print("Correct! You deal the enemy 1 health point of damage!")
        enemyHealth -= 1
        print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")
    else:
        print(f"Incorrect! The answer was {x * y}. You lose 1 health point")
        userHealth -= 1
        print(f"Your Health: {userHealth}, Enemy's Health: {enemyHealth}\n")

    return userHealth, enemyHealth


def enemyDrop(userInv, enemyCount):
    if enemyCount == 1 and userInv['Keys'] == 0:
        userInv['Keys'] = 1
        print('The enemy drops a key!')
    elif random.randint(0, 1) == 1 and userInv['Keys'] == 0:
        userInv['Keys'] = 1
        print('The enemy drops a key!')


enemyStats = {
    'Health': 0
}
