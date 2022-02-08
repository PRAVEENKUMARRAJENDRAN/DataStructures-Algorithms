def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] > query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
            break 
        elif result == 'left':
            print(cards[mid])
            hi = mid - 1
        elif result == 'right':
            print(cards[mid])
            lo = mid + 1
    return -1
    

cards = list(map(int, input("Enter the array elements with space between them:").strip().split()))
query = int(input("Enter the Number to be found"))

position = locate_card(cards,query)

if position == -1:
    print("The Card is not found inside the list")
else:
    print(position)
