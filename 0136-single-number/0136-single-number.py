class Solution:
    def singleNumber(self, nums):
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]