def countup(n):
	if n >= 10:
		print "Ok!"
	else:
		print n
		countup (n+1)
def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)

def countup(start, stop):
	if start > stop:
		print "Countup done!"
	else:
		print start
		countup(start + 1, stop)

def countdown(start, stop):
	if start < stop:
		print "Countdown done!"
	else:
		print start
		countdown(start - 1, stop)


def adder(stuff, total):
    if stuff == "":
        return total
    else:
        total += float(stuff) 
        stuff = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(stuff, total)

def main():
    out = adder(0, 0)
    print "The sum is " + str(out)
main()


def main():
	countup(1, 7)
	countdown(7, 1)
	return
main()

def biggest(n1, largest):
	if n1 == "":
		return largest 
	else:
		largest = float(n1) 
		n1 = raw_input("\nNext: ")
	if largest >
		return biggest( n1, largest)

def main():
	output = biggest(0, 0)

	print "The biggest number is " + str(output)
main()
	



	
