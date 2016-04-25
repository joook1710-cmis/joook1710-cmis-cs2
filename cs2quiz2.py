#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) if 
#b) and 
#c) or 
#
#2) What does 'return' do?
# gives out the output of the function 
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) if you do not indent there will be an error 
#b) return value will not bring out the correct output 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) square root of 3
#problem1_c) 0
#problem1_d) 5
#
#problem2_a) true
#problem2_b) false 
#problem2_c) false
#problem2_d) true 
#
#problem3_a) 0.3 (returning the C value)
#problem3_b) 0.5 (returning the B value)
#problem3_c) 0.5 (returning the A value)
#problem3_d) 0.5 (returning the B value)
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def comparing_numbers( a, b, c):
	a= num1
	b= num2
	c= num3 

def main():

	num1 = float(raw_input("Enter first number: "))
	num2 = float(raw_input("Enter second number: "))
	num3 = float(raw_input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
   largest == num1
elif (num2 > num1) and (num2 > num3):
   largest == num2
else:
   largest == num3

print "The largest number was",largest
 





main()

