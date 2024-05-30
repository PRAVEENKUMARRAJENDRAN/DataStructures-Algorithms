def removeDuplicates(nums: list[int]) -> int:
    index = 0

    for i in range(len(nums)):
        if nums[index] != nums[i]:
            nums[index+1] = nums[i]
            index +=1

    return index+1

print(removeDuplicates([1,1,1,3,4,4]))