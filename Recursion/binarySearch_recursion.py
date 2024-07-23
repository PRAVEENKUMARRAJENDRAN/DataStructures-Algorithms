

def binary_search(arr, target, low, high):
    if low > high:
        return False
    else:
        mid = (low+high)//2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, high)
        else:
            return binary_search(arr, target, low, mid-1)



arr = [1,2,3,4,5]
tar = 7
l,r = 0, len(arr) - 1
print(binary_search(arr, tar, l, r))