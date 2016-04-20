def countup(n):
	if n >= 6656:
		print "Blastoff!"
	else:
		print n
		countup (n+1)

def main():
	countup(1)
	return
main()
	
