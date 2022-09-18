def locate_card(cards,query):

	#initialize a position with value starting 0
	position = 0
     
    # A while loop with a conditon to check whether the position is less than length of the cards... 
	while(position < len(cards)):
		if(cards[position] == query):
			 #checking the position of the card number is equal to the query number...
             #if So we return the position...
			return position

		position += 1
	return -1


if __name__ == '__main__':
	#A input method to take array of integer input 
	cards = list(map(int, input("Enter the array elements with space between them:").strip().split()))



	query = int(input("Enter the Number to be found"))

	result = locate_card(cards,query)

	if(result != -1):
		print("The Number is found at",result,"position")

	else:
		print("The Number is not found in the Cards")






    





