def quicksort(array):
    left = []
    right = []
    equal = []
    

    if len(array) > 1:
        pivot = array[0]
        for i in range(len(array)):
            if array[i] < pivot:
                left.append(array[i])
            elif array[i] == pivot:
                equal.append(array[i])
            elif array[i] > pivot:
                right.append(array[i])
        return quicksort(left)+equal+quicksort(right)

 
        
    else:
        return array





if __name__ == '__main__':
    array = list(map(int,input('Enter the unsorted array').strip().split()))
    print(quicksort(array))