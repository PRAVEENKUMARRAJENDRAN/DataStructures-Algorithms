class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in nums:
            if i%3 != 0:
                operations += 1
        
        return operations
        