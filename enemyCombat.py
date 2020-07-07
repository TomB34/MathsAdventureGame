import character as char
import random

def initEnemy (enemyStatsDict):
    enemyStatsDict['Health'] = random.randint(4, 7)
    enemyStatsDict['Attack'] = random.randint(1, 4)
    enemyStatsDict['Defense'] = random.randint(1, 4)

def combatChoices(userchoices):
    userchoices.append("Stab")
    userchoices.append("Swipe")
    userchoices.append("Block")

def userStab():
    print('You stab the creature!')

enemyStats = {
    'Health': 0,
    'Attack': 0,
    'Defense': 0
}