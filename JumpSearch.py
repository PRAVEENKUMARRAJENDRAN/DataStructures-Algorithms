import math 

def jumpSearch(array,target):
    n = len(array)
    #Initialize the prev flag...
    prev = 0
    #Get the number of step to jump in the list
    step = math.sqrt(n)
    
    #A loop statement to find the block to searc....
    
    while array[int(min(step,n) - 1)] < target:
        prev =step
        step+=math.sqrt(n)
        print(prev,step,"block")
        if(prev >= n):
            return -1
    
    #A loop statement for linear search....
    while array[int(prev)] < target:
        prev+=1
        
        print(prev,step,"linear")
        if prev == min(step,n):
            return -1
    #A statement to check the value....        
    if array[int(prev)] == target:
        return int(prev)
        
    return -1
            
        
        
array = list(map(int,input("Enter the array elements").strip().split()))
target = int(input("Enter the value "))

position = jumpSearch(array,target)

print(position)
