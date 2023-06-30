def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        
        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -=1
    return arr




print(insertion_sort([4,2,6,5,1,3]))








"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while arr[j] > arr[i] and j > -1:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp 
            j -= 1 
    return arr

"""
print(insertion_sort([4,8,10,3,10]))