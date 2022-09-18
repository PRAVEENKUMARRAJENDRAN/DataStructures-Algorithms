def test_location(cards, query, mid):
    # first conditiion check whether the mid index is the element we need to find 
    if cards[mid] == query:
        return 'found'
    #checks whether we have to check left side or right side of the array
    # if the mid value is greater than query element we trace left side of the elements       
    elif cards[mid] > query:
        return 'left'
    # if the mid value is lesser than query element we trace right side of the elements
    else:
        return 'right'

def locate_card(cards, query):
    #lower index is 0 position and higher index is length - 1 position
    lo, hi = 0, len(cards) - 1
    #checks whether the index of lower is lesser than or equal to higher
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        # IF we get the found from the test_location func we return the mid value
        if result == 'found':
            return mid
            break 
        #If left we minus the mid value to 1 and assign to hi 
        elif result == 'left':
            print(cards[mid])
            hi = mid - 1
        #If right we plus the mid value with 1 and assign to lo
        elif result == 'right':
            print(cards[mid])
            lo = mid + 1
    return -1
    
#We are getting the input of cards as array
# where list is consider as array in python
#Strip function is used to remove space in the begining and end of the string..
#It split the words as array...
cards = list(map(int, input("Enter the array elements with space between them:").strip().split()))
query = int(input("Enter the Number to be found"))

position = locate_card(cards,query)

if position == -1:
    print("The Card is not found inside the list")
else:
    print("The place of the card is",position)
