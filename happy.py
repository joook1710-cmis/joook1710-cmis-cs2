def clapYourHands():
    print "clap clap"
def stompYourFeet():
    print "stomp stomp"
def main():

	question = raw_input("Are you happy? (Y or N): ") == "Y"
	question2 = raw_input("And you know it?: (Y or N): ") == "Y" 
	
	youreHappy = True
	youKnowIt = True 

	if youreHappy and youKnowIt:
		clapYourHands()
		stompYourFeet()

	print "Good bye"
main()
