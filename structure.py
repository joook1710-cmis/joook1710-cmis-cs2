import math
def exp(e, x):
    return e ** x
def output (name, e, x, y):
    out = """

Hey! My favorite color is {} !
Did you know:
{} ** {} = {}
""".format(name, e, x, y)
    return out

def main():
	#input selection
	name= raw_input("What is your favorite color? : ")
	e= int(raw_input("Type a number: "))
	x= int(raw_input("Type another: "))
	#processing
	y= exp(e, x)
	#output 
	out = output(name, e, x, y)
	print out

main()

def vel
d= 400
t= 8 
def main():
	#input selection
	name= raw_input("What's your name?: ")
	d= raw_input( "Type the miles you traveled: ")
	t= raw_input( "Type how long it took: ") 
	
