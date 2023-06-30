


def linear_search(arr, value):

    for i in range(len(arr)):
        if arr[i] == value:
            return "The value {} is present".format(value)
        
    return "The value {} is not present".format(value)


print(linear_search([2,4,5,6,7], 10))
