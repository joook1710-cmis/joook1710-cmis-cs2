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
	# v = volume
	v1= int(raw_input("The volume of Cube one : "))
	v2= int(raw_input("The volume of Cube two: "))
	v3= int(raw_input("The volume of Cube three: "))
	#processing
	totalVolume= totals(v1, v2, v3)
	#output 
	out = output(v1, v2, v3, totalVolume)
	print out

main()


	
