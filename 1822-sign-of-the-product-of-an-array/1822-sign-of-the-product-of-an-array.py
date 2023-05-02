class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # nums.sort()
        # if len(nums)==1:
        #     if nums[0]==0:
        #         return 0
        #     elif nums[0]>1:
        #         return 1
        #     else:
        #         return -1
        # l,h=0,len(nums)-1
        # while l<h:
        #     mid=(l+h)//2
        #     if nums[mid]==0:
        #         return 0
        #     elif nums[mid]<0:
        #         l=mid+1
        #     else:
        #         h=mid
        # if l&1:
        #     return -1
        # return 1
        x=0
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                x+=1
            else:
                continue
        if x&1:
            return -1
        return 1