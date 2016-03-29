#You are trapped in a cage. You need to find the right key that has enough power to break the door of the cage. However the monster who is guarding you will also use some kind of key to lock you up. If you choose the key that is more powerful that the key the monster uses then you will win. However if the mosnster chooses a key that is more powerful that yours then the monster will win. 
import random 
def eat(item):

    if item == "red":
        strength = 0    
    elif item == "orange":
        strength = 1
    elif item == "yellow":
        strength = 2
    elif item == "green":
        strength = 3
    elif item == "blue":
        strength = 4
    elif item == "brown":
        strength = 5
    elif item == "purple":
        strength = 6
    elif item == "back":
        strength = 7
    elif item == "white":
        strength = 8
    elif item == "mint":
        strength = 9
    elif item == "pink ":
        strength = 10
    else:
        strength = random.randint(0,10)
    return strength * random.random()

def getAttackValue():
 
    number = int(raw_input("Type attack value (0-99): "))
    if number > 99 or number < 0:
        number = random.randint(0, 99)
    attackValue = float(number)/100
    return attackValue    

def wrestle(playerKeyPower, monsterKeyPower, playerAttackKeyValue):

    targetValue = random.random()
    playerAttackResult = playerKeyPower + abs(playerAttackKeyValue - targetValue)    
    enemyAttackResult =  monsterKeyPower + targetValue
    if playerAttackResult > enemyAttackResult:
        return True
    else:
        return False

def resultTemplate(playerKeyPower, monsterKeyPower, result):

    if result == True:
        msg = "wins"
    else:
        msg = "loses"
    return """
Player strength: {}
Enemy strength: {}
Player {}!
""".format(playerKeyPower, monsterKeyPower, msg)

def main():


    playerColor = raw_input("What colored key would you like to pick? ")
    monster1Color = raw_input("What colored key does monster 1 pick? ")
    monster2Color = raw_input("What colored key does monster 2 pick? ")

    playerKeyPower = color(playerFood)
    monster1KeyPower = color(enemy1Food)
    monster2KeyPower = color(enemy2Food)

    playerAttackValue1 = getAttackValue()
    result1 = wrestle(playerKeyPower, enemy1Strength, playerAttackKeyValue1)

    playerAttackValue2 = getAttackValue()   
    result2 = wrestle(playerKeyPower, enemy2Strength, playerAttackKeyValue2)
    
    output = """
You picked the {} colored key.
Monster 1 picked the {} colored key.
Monster 2 picked the {} colored key.
""".format(playerFood, enemy1Food, enemy2Food)
    output += resultTemplate(playerKeyPower, enemy1Strength, result1)
    output += resultTemplate(playerKeyPower, enemy2Strength, result2)

    print output
