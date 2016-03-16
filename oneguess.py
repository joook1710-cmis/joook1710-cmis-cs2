import random
import math
def guessNumber():
	number =  int(raw_input("Type any number(0-10):"))
	if number > 10 or number < 0:
		number = random.randint(0, 10)
	numberValue = float(number)/10
	return numberValue

def output(minnumber, maxnumber):
	number= minnumber
	number2= maxnumber
	return """

I am thinking of a number from {} to {}
What do you think it is?: 

""".format(minnumber, maxnumber)
	return output

def minGuess(comp_number, your_number, difference):
	minGuess= """
The target was ()
Your guess was ()
That is under by ()
""".format(comp_number, your_number, outcome)
	return minGuess
def maxGuess(comp_number, your_number, outcome):
	maxGuess= """
The target was ()
Your guess was ()
That is under by ()
""".format(comp_number, your_number, outcome)
	return maxGuess
def correctGuess(comp_number, your_number, outcome):
	correctGuess= """
The target was ()
Your guess was ()
That is under by ()
""".format(comp_number, your_number, outcome)
	return correctGuess 

def main():
	number= int(raw_input("What is the minimum number?: "))
	number2= int(raw_input("What is the maximum number?: "))
	number3= int(raw_input("I'm thinking of a number from" + str(maximum) + ". \n" + "What do you think it is?: "))

	comp_number = int(random.randint (big, small))
	outcome= abs(sub(int(your_guess), comp_number))
	if comp_number < str(abs(int(your_number))):
		minGuess = minGuess(comp_number, your_number, outcome)
		print minGuess
	elif comp_number > str(abs(int(outcome))):
		maxGuess(comp_number, your_number, outcome)
		print maxGuess 
	elif comp_number == abs(int(outcome)): 
		correctGuess = (comp_number, your_number, outcome)
		print correctGuess 
main()



