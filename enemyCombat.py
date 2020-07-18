import character as char
import random

def initEnemy (enemyStatsDict):
    enemyStatsDict['Health'] = random.randint(4, 6)
    enemyStatsDict['Attack'] = random.randint(2, 4)
    enemyStatsDict['Defence'] = random.randint(3, 5)

def combatChoices(userchoices):
    userchoices.append("Stab")
    userchoices.append("Swipe")
    userchoices.append("Block")

def userStab(userHealth, userAttack, enemyHealth, enemyDefence):
    # Dice is rolled.
    diceRoll = random.randint(1, 4)
    stabVal = enemyDefence - userAttack

    # If user doesn't beat enemy, user potentially loses health.
    if stabVal < diceRoll:
        if random.randint(0, 1) == 0:
            print('You fail to stab the creature!')
        else:
            userHealth -= 1
            print('You fail to stab the creature and it hurts you! -1 health.' )

    # If users draws or is +2 above enemy defense, enemy loses 1 health.
    elif stabVal >= diceRoll and stabVal <= diceRoll + 2:
        enemyHealth -=  1
        print('You stab the creature! -1 health.')

    # If user is higher by +3, critical hit and enemy loses 2 health.
    elif stabVal > diceRoll + 2:
        enemyHealth -= 2
        print('You stab the creature and it is critical! -2 health.')

    return userHealth, enemyHealth

def userSwipe(userHealth, userAttack, enemyHealth, enemyDefence):
    diceRoll = random.randint(1, 8)
    swipeVal = userAttack - enemyDefence

    # If user fails, loses health
    if swipeVal < diceRoll:
        userHealth -= 1
        print('You fail to swipe the enemy. -1 health.')
    # If user draws or is +2 above enemy defence, enemy loses 2 health.
    elif swipeVal >= diceRoll and swipeVal <= diceRoll + 2:
        enemyHealth -= 2
        print('You swipe the enemy with your sword! -2 health.')
    # If user is higher by +3, critical hit and enemy loses 3 health
    elif swipeVal > diceRoll + 2:
        enemyHealth -= 3
        print('A critical swipe! -3 health.')

    return userHealth, enemyHealth

def userBlock(userHealth, userDefence, enemyAttack):
    diceRoll = random.randint(1, 4)
    enemyAttackValue = enemyAttack - userDefence

    # If enemy fails, noone loses health
    if enemyAttackValue < diceRoll:
        if random.randint(0, 1) == 0:
            print("You defend against the enemy's attack!")
        else:
            print("You defend yourself very well! +1 health")
            userHealth += 1
    # If enemy draws or is +2 above user's defence, -1 health for user
    elif enemyAttackValue >= diceRoll and enemyAttackValue <= diceRoll + 2:
        print("Your defence fails! -1 health.")
        userHealth -= 1
    # If enemy roll is +3 above user defence, -2 health for user
    elif enemyAttackValue > diceRoll + 2:
        print("The enemy's attack is critical! -2 health.")
        userHealth -= 2

    return userHealth

enemyStats = {
    'Health': 0,
    'Attack': 0,
    'Defense': 0
}