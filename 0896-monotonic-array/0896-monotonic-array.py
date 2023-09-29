class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ac=nums.copy()
        
        ac.sort()
        print(ac,ac[::-1],nums)
        if nums==ac or nums==ac[::-1]:
            return True
        else:
            return False