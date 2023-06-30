def helper(arr, value, mid):
    if arr[mid] == value:
        return 'found'
    elif arr[mid] < value:
        return 'right'
    elif arr[mid] > value:
        return 'left'
    

def binary_search(arr, value):
    l,r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r) // 2

        result = helper(arr, value, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            r = mid - 1
        elif result == 'right':
            l = mid + 1
    return None 

arr = [1, 5, 7, 9, 10]
value = 9

print(binary_search(arr, value))
