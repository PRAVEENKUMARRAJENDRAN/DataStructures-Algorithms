class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        number_of_good_pairs = 0

        for i in nums:
            if i in h:
                number_of_good_pairs += h[i]
                h[i] += 1
            else:
                h[i] = 1
        return number_of_good_pairs
