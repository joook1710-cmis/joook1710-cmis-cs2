# Recursive Function makes a function repeat itself. (+1)
# The resursive function would not stop. (+1)
# The base case and the recursive case. (+1)
# By using ":". You have to tab everything in as well. (-1)
# By using "return" or "print". (-1)

#a1 = 8 (1)
#a2 = 8 (1)
#a3 = -1 (1)

#b1 = 2 (1)
#b2 = 2 (1)
#b3 = 4 (1)

#c1 = -2 (1)
#c2 = 4 (1)
#c3 = 45 (1)

#d1 = 6 (1)
#d2 = 8 (1)
#d3 = 4 (1)

def average_odd_numbers(sum, ct):
    n = raw_input("Next: ")
    if n == "":
        #BASE CASE
        return sum/ct
    else:
        #RECURSIVE CASE
        n = float(n)
        if n % 2 == 1:
            sum += n
            ct += 1
        return average(sum, ct)
def main():
    a = average(0.0 ,0.0)
    print "The average of your odd numbers was {}.".format(a)
main()
