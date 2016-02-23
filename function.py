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
	return float(q / w)
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
#string as an argument and returns a message box
def msg_box(word):
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word)+ (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+"
print msg_box("Hello")
print msg_box("I eat cats!")

#calling functions
add1= add(5,6)
add2= add(6,3)
sub1= sub(9,3)
sub2= sub(5,4)
mul1= mul(2,3)
mul2= mul(2,4)
div1= div(5,3)
div2= div(7,4)
hoursfromsec1= hours_from_seconds_div(97000,4800)
hoursfromsec2= hours_from_seconds_div(87000,4800)
circlearea1= circle_area(4)
circlearea2= circle_area(9)
spherevolume1= sphere_volume(8)
spherevolume2= sphere_volume(3)
averagevolume1= avg_volume(6,4)
averagevolume2= avg_volume(4,4)
area1= area(1,2,3)
area2= area(4,5,6)
rightalign1= right_align("LOL")
rightalign2= right_align("YEAA")
center1= center("hahaha")
center2= center("What")
msgbox1= msg_box("Poop")
msgbox2= msg_box("yo")

#printing the functions
print msg_box (str(add1))
print msg_box (str(add2))
print msg_box (str(sub1))
print msg_box (str(sub2))
print msg_box (str(mul1))
print msg_box (str(mul2))
print msg_box (str(div1))
print msg_box (str(div2))
print msg_box (str(hoursfromsec1))
print msg_box (str(hoursfromsec2))
print msg_box (str(circlearea1))
print msg_box (str(circlearea2))
print msg_box (str(spherevolume1))
print msg_box (str(spherevolume2))
print msg_box (str(averagevolume1))
print msg_box (str(averagevolume2))
print msg_box (str(area1))
print msg_box (str(area2))
print msg_box (str(rightalign1))
print msg_box (str(rightalign2))
print msg_box (str(center1))
print msg_box (str(center2))
print msg_box (str(msgbox1))
print msg_box (str(msgbox2))
