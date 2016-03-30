import math
def exp(e, x):
    return e ** x
def volumeOfSphere(v):
	volume = float(4)/3 * math.pi * (v**3)
def totals(a, b, c):
	return int(a + b + c)
def output (a, b, c, d):
	out = """
There are three cubes on the table. Sphere One has a volume of {}, Sphere Two has a volume of {}, Sphere Three has a volume of {}. The total volume of three cubes are {}. 
""". format(a, b, c, d)
	return out 

def main():
	#input selection
	# v = volume
	v1= int(raw_input("The volume of sphere one : "))
	v2= int(raw_input("The volume of sphere two: "))
	v3= int(raw_input("The volume of sphere three: "))
	#processing
	totalVolume= totals(v1, v2, v3)
	volumeOfSPhere= totals(v1, v2, v3)
	#output 
	out = output(v1, v2, v3, totalVolume, volumeOfSphere)
	print out
	

main()


	
