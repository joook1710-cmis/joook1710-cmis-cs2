#You are trapped in a cage. You need to find the right key that has enough power to break the door of the cage. However the monster who is guarding you will also use some kind of key to lock you up. If you choose the key that is more powerful that the key the monster uses then you will win. However if the mosnster chooses a key that is more powerful that yours then the monster will win. 
import random 
def key_color(item):

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

def key_shape(item):

	if item == "circle"
		strength = 5
	elif item == "triangle" 

def getKickValue():
 
    number = int(raw_input("Type Karate kick power (0-10): "))
    if number > 10 or number < 0:
        number = random.randint(0, 10)
    KickValue = float(number)/100
    return KickValue    

def wrestle(playerKeyPower, monsterKeyPower, playerAttackKeyValue):

    targetValue = random.random()
    playerAttackResult = playerKeyPower + abs(playerAttackKeyValue - targetValue)    
    monsterAttackResult =  monsterKeyPower + targetValue
    if playerAttackResult > monsterAttackResult:
        return True
    else:
        return False

def resultTemplate(playerKeyPower, monsterKeyPower, result):

    if result == True:
        msg = "are free"
    else:
        msg = "are still stuck in the cage"
    return """
Your key power: {}
Monster's key power: {}
You {}!
""".format(playerKeyPower, monsterKeyPower, msg)

def main():


    playerColor = raw_input("What colored key would you like to pick? ")
    monster1Color = raw_input("What colored key does monster Koola pick? ")
    monster2Color = raw_input("What colored key does monster Kooko pick? ")

    playerKeyPower = key_color(playerColor)
    monster1KeyPower = key_color(monster1Color)
    monster2KeyPower = key_color(monster2Color)

    playerAttackValue1 = getKickValue()
    result1 = wrestle(playerKeyPower, monster1KeyPower, playerAttackValue1)

    playerAttackValue2 = getKickValue()   
    result2 = wrestle(playerKeyPower, monster2KeyPower, playerAttackValue2)
    
    output = """
You picked the {} key.
Monster Koola picked the {} key.
Monster Kooko picked the {} key.
""".format(playerColor, monster1Color, monster2Color)
    output += resultTemplate(playerKeyPower, monster1KeyPower, result1)
    output += resultTemplate(playerKeyPower, monster2KeyPower, result2)

    print output
main()
