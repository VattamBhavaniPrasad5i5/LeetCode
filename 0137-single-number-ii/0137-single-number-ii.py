class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        n=set(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in n:
            if d[i]==1:
                return i