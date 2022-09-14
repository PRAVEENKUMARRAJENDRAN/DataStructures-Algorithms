def InsertionSort(array):
    for i in range(1,len(array)):
        anchor = array[i]
        j = i - 1
        while j >= 0 and anchor < array[j]:
            array[j+1] = array[j]
            j = j - 1
        print(j)
        array[j+1] = anchor 
    print(array)




if __name__ == '__main__':
    array = list(map(int,input("Enter unsorted array").strip().split()))
    InsertionSort(array)
