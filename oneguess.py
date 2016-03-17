import random
import math


def main():
	minimum= int(raw_input("What is the minimum number?: "))
	maximum= int(raw_input("What is the maximum number?: "))

	output = """ I'm thinking of a number between {} and {}. """.format (minimum, maximum)
	print output 

	number = random.randint(int(minimum), int(maximum))
	your_number = raw_input("Guess the number:")
	output = """ The number was {}: """.format(number)
	print output
	output = """ Your guess was {}: """.format(your_number)

if your_number == number:
	return True
	output = " Congratulations, you guessed the number correctly"		
	print output


	if your_number > number:
		difference = int(your_number) -  int(number)
		
	output = """ Thats {} higher than the number """.format(difference)
	print output	
	
	if your_number < number:
		more_than = int(number) - int(number)
		
	output = """ Your guess was under by {}  """.format(more_than)
	print output 

main()


