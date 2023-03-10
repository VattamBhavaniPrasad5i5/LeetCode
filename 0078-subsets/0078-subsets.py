class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in nums:
            ans+=[l+[i] for l in ans]
        return ans