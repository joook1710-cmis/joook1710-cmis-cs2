#def countdown(x):
 #   while x > -1:
  #      print x
   #     x -= 1

#countdown(10)
#countdown(20)

#def counter(x):
 #   while x>0: 
  #      print x
   #     x -= 1
    #while x<0:
     #   print 
      #  x += 1

#counter(10)
#counter(-3)

#def countfrom(x, y): 
#	if x < y:
#		while x <= y:
#			print x 
#			x += 1 
#	else y < x:
#		while y <= x:
#			print y
#			y += 1 
#countfrom(-10, 10)

#def sum_of_odds(n):
#n is positive or negative 
#each n is even or odd 
#counting from n to 0 
#sum of the odds 
#	total = 0 
#	if n > 0:
#		while n > 0: 
#			if n % 2 == 1:
#				total += n 
#			n -= 1                                             
#	elif n < 0: 
#		while n < 0 :
#			if n % 2 == 1: 
#				total += n 
#			n += 1 
#print sum_of_odds(10)
 
def grid(w, h): 
	out = ""
	while w > 0:
		out += "."
		w -= 1
	return out 


grid(3, 4)


