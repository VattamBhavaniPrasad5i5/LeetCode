class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """n=len(nums)
        arr=[0]*(n)
        ind=0
        for i in range((n)//2):
            arr[ind]=nums[i]
            arr[ind+1]=nums[i+(n//2)]
            ind+=2
        return arr"""
        ans=[]
        n=len(nums)
        for i in range(n//2):
            ans.append(nums[i])
            ans.append(nums[i+(n//2)])
        return ans
            
        