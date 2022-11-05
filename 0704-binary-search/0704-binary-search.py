class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f=0
        for i in range(len(nums)):
            if nums[i]==target:
                f=1
                return i
        if f==0:
            return '-1'
            
        