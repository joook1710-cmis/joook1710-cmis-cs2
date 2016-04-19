import random
import math 

print ("This  program will ask you for 5 integer or float values.It will calculate the average of all values from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd.")



def main():
    n0 = float(raw_input("n0:"))
    n1 = float(raw_input("n1:"))
    n2 = float(raw_input("n2:"))
    n3 = float(raw_input("n3:"))
    n4 = float(raw_input("n4:"))
    n5 = float(raw_input("n5:"))
	
#processing
    average = (n0+n1+n2+n3+n4+n5)/5
#output
    if n0 > 0 and n0 < 10:
        print (int(n0)) ("is in range.")
    elif n0 < 0 or n0 > 10: 
        print (int(n0)) ("is out of the range.")

    if n1 > 0 and n1 < 10:  
        print (int(n1)) ("is in range.")
    elif n1 < 0 or n1 > 10: 
        print (int(n1)) ("is out of the range.")

    if n2 > 0 and n2 < 10:
        print (int(n2)) ("is in range.")
    elif n2 < 0 or n2 > 10: 
        print (int(n2)) ("is out of the range.")

    if n3 > 0 and n3 < 10:
        print (int(n3)) ("is in range.")
    elif n3 < 0 or n3 > 10: 
        print (int(n3)) ("is out of the range.")

    if n4 > 0 and n4 < 10:
        print (int(n4)) ("is in range.")
    elif n4 < 0 or n4 > 10: 
        print (int(n0)) ("is out of the range.")

    if n5 > 0 and n5 < 10:
        print (int(n5)) ("is in range.")
    elif n5 < 0 or n5 > 10: 
        print (int(n5)) ("is out of the range.")

main()
