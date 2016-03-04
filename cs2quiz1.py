#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# assign value to variable 
# +1 point
#
#2 3pts) Write a technical definition for 'function'
# Function is a named sequence of statements that performs a computation. 
# When you define a function, you specify the name and the sequence of statements. 
# +3 points 
#
#3 1pt) What does the keyword "return" do?
# When a function is called, the program stops and waits for the user to type something. When the user presses return, the program resumes and the output comes out. 
# +1 point 
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: String
# "Hello world" , "I love you"  
#	2: Tuple
# ("Hello", "Yo", 44) , (1, 2, 3, 4)
#	3: Boolean 
# true false  
#	4: Integer
# 4 , 5
#	5: Floating point 
# 0.1, 3.7 
# +5 points 
 
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# Function call operator is used for operations that require a number of parameters. This works because expression list is a list instead of a single operand. 
# Programming languages come with a prewritten set of functions that are kept in a library. And function definition is used to describe what is kept in the library. 
# +2 points 
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input 
# Collection refers to gathering the data from a variety of sources and assembling it. Verification means checking the data to determine whether it is accurate and complete. 
#	2: Process
# one or more of tasks may be performed on the input data. 
#	3: Output 
# Data are organized by characteristics meaninggul to the user. The user needs to call the function to bring out the output.
# +3 points 
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#1 pt for header line
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name

import math 
def radiusFromArea(area):
	radius = math.sprt (float(area)/math.pi)
	return radius

#1 header line
#1 parameter names
#0.5 output format

def output(d1,d2,d3):
	out = 

#1 header line
#1 input
#1 converting input
#1 calling output function
#2 correct diameter formula
#1 variable names 

#input
def main():
	c1= float(raw_input("Area of c1: "))
	c2= float(raw_input("Area of c2: "))
	c3= float(raw_input("Area of c3: "))

	r1= radiusFromArea(c1)
	r2= radiusFromArea(c2)
	r3= radiusFromArea(c3)
#processing

	d1= r1*2
	d2= r2*2
	d3= r3*2

#output

print output(d1,d2,d3)

	
#1 calling function 	
main()

#1 explanatory comments 
#0.5 code format 



#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


