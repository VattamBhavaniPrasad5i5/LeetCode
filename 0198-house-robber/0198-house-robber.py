class Solution:
    def rob(self, nums: List[int]) -> int:
        b=[]
        l=len(nums)
        if  l==1:
            return nums[0]
        if l==2:
            return max(nums[0],nums[1])
        if l>1:
            b=[nums[0],nums[1]]
        for i in range(2,l):
            b.append(0)
        i=0
        while(i<l-1):
            
            if i<l-2:
                b[i+2]=max(b[i+2],nums[i]+nums[i+2])
                
            if i<l-3:
                b[i+3]=max(b[i+3],nums[i]+nums[i+3])
            if i>0:
                nums[i+1]=b[i+1]
            i=i+1
        return max(b[l-1],b[l-2])
            
        