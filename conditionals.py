#conditional execution: The boolean expression after the if statement. We end the if statement with a colon character and the lines after the if statement are indented.
#alternative execition: two possibilites and the condition determines which one gets executed. (else)
#chained conditionals: more than two possibilies and the conditions (elif, else)
#You are trapped in a cage. You need to find the right key that has enough power to break the door of the cage. However the monster who is guarding you will also use some kind of key to lock you up. If you choose the key that is more powerful that the key the monster uses then you will win. However if the mosnster chooses a key that is more powerful that yours then the monster will win. 
def playerKeyColor():

    if color == "red":
        power = 0    
    elif color == "orange":
        power = 1
    elif color == "yello":
        power = 2
    elif color == "green":
        power = 3
    elif color == "blue":
        power = 4
    elif color == "brown":
        power = 5
    elif color == "purple":
        power = 6
    elif color == "pink":
        power = 7
    elif color == "white":
        power = 8
    elif color == "maroon":
        power = 9
    elif color == "black":
        power = 10
    else:
        strength = random.randint(0,10)
    return strength * random.random()

def monsterKeyColor():
	if color == "red":
		power = 0    
	elif color == "orange":
		power = 1
	elif color == "yello":
		power = 2
	elif color == "green":
		power = 3
	elif color == "blue":
		power = 4
	elif color == "brown":
		power = 5
	elif color == "purple":
		power = 6
	elif color == "pink":
		power = 7
	elif color == "white":
		power = 8
	elif color == "maroon":
		power = 9
	elif color == "black":
		power = 10
	else:
		strength = random.randint(0,10)
	return strength * random.random()


def keyPowerValue():
 
    number = int(raw_input("Type attack value (0-99): "))
    if number > 99 or number < 0:
        number = random.randint(0, 99)
    attackValue = float(number)/100
    return attackValue    

def wrestle(playerKeyPower, monsterKeyPower, keyPowerValue):

    targetValue = random.random()
    playerKeyPower = playerStrength + abs(playerKeyPower - targetValue)    
    monsterKeyPower =  enemyStrength + targetValue
    if playerKeyPower > monsterKeyPower:
        return True
    else:
        return False

def resultTemplate(playerKeyPower, monsterKeyPower, result):

    if result == True:
        msg = "wins"
    else:
        msg = "loses"
    return """
Player's key strength: {}
Monster's key strength: {}
Player {}!
""".format(playerStrength, enemyStrength, msg)


def main():


    playerKeyColor = raw_input("What colored key are you going to choose? ")
    monsterKeyColor = raw_input("What colored key is the monster going to choose? ")
   

playerKeyPower = playerKeyColor
monsterKeyPower = monsterKeyColor
    

playerAttackValue1 = keyPowerValue()
result1 = wrestle(playerKeyPower, monsterKeyPower, playerAttackValue1)

    
output = """
You chose the {} key.
The monster chose the {} key.
""".format(playerFood, enemy1Food, enemy2Food)
output += resultTemplate(playerStrength, enemy1Strength, result1)
   

print output
main()
