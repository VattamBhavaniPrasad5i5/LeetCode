class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

#         max_len=0
#         if nums.count(0)==0:
#             return len(nums)-1
#         for i in range(len(nums)):
#             c=0
#             l=0
#             for j in range(i,len(nums)):
#                 if nums[j]==0:
#                     c+=1
                    
#                 if c<2 :
#                     l+=nums[j]
#                 if c==2:
#                     break
#             if l>max_len and l!=len(nums)-1:
#                 max_len=l
#         return max_len
        if 1 not in nums: 
            return 0
        if 0 not in nums:
            return len(nums)-1
        
        nums=list(map(len,''.join(map(str,nums)).split('0')))
        print(nums)
        return max(map(sum,zip(nums, nums[1:])))
            
    