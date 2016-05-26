def countdown(x):
    while x > -1:
        print x
        x -= 1

countdown(10)
countdown(20)

def counter(x):
    while x>0: 
        print x
        x -= 1
    while x<0:
        print 
        x += 1

counter(10)
counter(-3)

def countfrom(x, y): 
	if x < y:
		while x <= y:
			print x 
			x += 1 
	else y < x:
		while y <= x:
			print y
			y += 1 
countfrom(-10, 10)

def sum_of_odds(n): 
	total = 0
	if n < 0:
		while float(n) % 2 == 1:
			n += 1
			print total
 
