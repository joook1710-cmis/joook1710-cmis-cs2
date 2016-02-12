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
	return ((1.0/6 * 3.14159265359 * a**3) + (1.0/6 * 3.14159265359 * b**3)) /2

print avg_volume (10,20) 

#Representation of the 3 side lengths of a triangle 
def area(a,b,c): 
	n= (a+b+c)/2
	return (n*(n-a)*(n-b)*(n-c))**0.5

print area(1, 2, 2.5)

#Making a string an agrument and returnng it as a work with additional space
def right_align(word):
	return (80-len(word))*(" ") + word
print right_align( "Hello" )

#String as an agrument that is centered
def center(word):
	return (40-len(word))*(" ") + word
print center("Hello")

#Message box
def msg_box(word):
	return "+" + (len(word)) *4 

