class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_pos=0
        distance=0
        jumps=0
        for i in range(len(nums)-1):
            distance=max(distance,i+nums[i])
            if curr_pos==i:
                jumps+=1
                curr_pos=distance
        return(jumps)     