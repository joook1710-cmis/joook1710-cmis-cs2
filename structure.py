import math
def exp(e, x):
    return e ** x
def volumeOfCube(v):
	volume = (4/3) * math.pi * (v**3)
def totals(a, b, c):
	return int(a + b + c)
def output (a, b, c, d):
	out = """
There are three cubes on the table. Cube One has a volume of {}, Cube Two has a volume of {}, Cube Three has a volume of {}. The total volume of three cubes are {}. 
""". format(a, b, c, d)
	return out 

def main():
	#input selection
	# r = radius
	r1= raw_input("The radius of Sphere one : ")
	r2= int(raw_input("The radius of Sphere two: "))
	r3= int(raw_input("The radius of Sphere three: "))
	#processing
	totalVolume= totals(r1, r2, r3)
	#output 
	out = output(r1, r2, r3, totalVolume)
	print out

main()


	
