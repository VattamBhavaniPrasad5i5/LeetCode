class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=set(nums)
        arr=[]
        for i in a:
            if nums.count(i)>(n/3):
                arr.append(i)
        return arr
        