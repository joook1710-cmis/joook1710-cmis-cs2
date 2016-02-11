#Added two arguements 
def add(a,b):
	return a + b 
c = add(3, 4)
print c

#Subtraction two arguements 
def sub(j,k):
	return j - k
l = sub(5, 3)
print l 

#Multiplied two arguements 
def mul(r,t):
	return r * t
e = mul(4,4)
print e

#Divided two arguements
def div(q,w):
	return q / w
y = div(2,3)
print y 

#Defined hours from seconds 
def hours_from_seconds_div(a,b):
	return a/b
s = div(86400, 3600) 
print s

#Representation of a radius of a circle 
def circle_area(r):
	return 3.14159265359 * (r**2)
print circle_area(5) 

#Representation of a volume of the sphere
def sphere_volume(v):
	return 3.14159265359 * 1.333333333333 * (v**3)
print sphere_volume(5)

#Representation of the average of the volumes 
def avg_volume(a,b):
	return ((4/3)*3.14159265359*a**3) + ((4/3)*3.14159265359*b**3)/2
print avg_volume(10,20)
