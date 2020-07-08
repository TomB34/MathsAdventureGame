import character as char
import random

def initEnemy (enemyStatsDict):
    enemyStatsDict['Health'] = random.randint(4, 7)
    enemyStatsDict['Attack'] = random.randint(1, 4)
    enemyStatsDict['Defence'] = random.randint(1, 4)

def combatChoices(userchoices):
    userchoices.append("Stab")
    userchoices.append("Swipe")
    userchoices.append("Block")

def userStab(userHealth, userAttack, enemyHealth, enemyDefence):
    # Attack and defense for user and enemy are set based on stats
    # Dice is rolled.
    diceRoll = random.randint(1, 6)
    stabVal = diceRoll + userAttack

    # If user doesn't beat enemy, user potentially loses health.
    if stabVal < enemyDefence:
        if random.randint(0, 1) == 0:
            print('You fail to stab the creature!')
        else:
            userHealth -= 1
            print('You fail to stab the creature and it hurts you!')
    # If users draws or is +2 above enemy defense, enemy loses 1 health.
    elif stabVal >= enemyDefence and stabVal <= enemyDefence + 2:
        enemyHealth -=  1
        print('You stab the creature!')

    # If user is higher by +3, critical hit and enemy loses 2 health.
    elif stabVal >= enemyDefence + 2:
        enemyHealth -= 2
        print('You stab the creature and it is critical!')

    return userHealth, enemyHealth

enemyStats = {
    'Health': 0,
    'Attack': 0,
    'Defense': 0
}