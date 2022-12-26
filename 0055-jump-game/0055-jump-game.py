class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)
        i = curr_max=0
        while(i<l - 1):
            curr_max=max(curr_max,i+nums[i])
            if i<curr_max:
                i+=1
            else:
                return False
        return True
                
            
            
        
        
            
            
        