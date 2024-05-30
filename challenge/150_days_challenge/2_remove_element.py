
def remove_element(nums: list[int], val: int) -> int:
    arr_len = len(nums)

    i = 0 

    while i <= arr_len-1:
        if nums[i] == val:
            del(nums[i])
            arr_len -= 1
            i -= 1
        i += 1
    
    print(arr_len, nums)


remove_element([0,1,2,2,3,0,4,2], 2)