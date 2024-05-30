def removeDuplicates(nums: list[int]) -> int:

    index = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[index-2]:
            nums[index] = nums[i]
            index += 1

    return index

print(removeDuplicates([1,1,1,2,2,3,4,4,4]))