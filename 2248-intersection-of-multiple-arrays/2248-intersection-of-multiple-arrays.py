class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l=len(nums)
        a=[]
        for i in nums:
            a+=i
        arr=[]
        for i in a:
            if a.count(i)==l and i not in arr:
                arr.append(i)
        arr.sort()
        return arr
            
    