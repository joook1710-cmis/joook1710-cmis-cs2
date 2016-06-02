import random

def Guessing_Number(Number, Total):

    GuessNumber = int(raw_input("Guess a number: "))
    if GuessNumber  == Number:
        print "You got the answer in " + str(Total) + " tries."
    elif GuessNumber  == Number:
        print "GoodJob!!"
    elif GuessNumber  > Number:
        print "Too High!!"
        Guessing_Number(Number, Total + 1)
    else:
        print "Too Low!!"
        Total + 1
        Guessing_Number(Number,Total + 1)

Guessing_Number(random.randint(1, 10), 0)


