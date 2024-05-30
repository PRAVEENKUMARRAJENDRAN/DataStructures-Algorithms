"""
two asc sorted array
nums1 and nums2 
m is number of values in the array nums1
n is number of values in the array nums2


example 
nums1 = [1,2,3,0,0,0]
nums2 = [1,5,6]
n,m = 3,3

//Output
[1,1,2,3,5,6]

"""

def merge_array(nums1: list[int], n: int, nums2: list[int], m: int) -> list[int]:
    # we are defining the whole length of the two arrays
    last = m + n -1

    while m > 0 and n > 0:
        if nums1[m -1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n-1]
        n,last = n -1, last-1

    return nums1

print(merge_array([1,2,3,0,0,0], 3, [1,5,6], 3))