class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=set(nums)
        for i in n:
            if nums.count(i)==1:
                return i