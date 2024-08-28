class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        #ans = [None] * len(nums)
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
        


if __name__  == '__main__':
    s = Solution()

    print(s.buildArray([0,2,1,5,3,4]))