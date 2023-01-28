class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=[]
        print(d)
        for i in d:
            if d[i]==1:
                a.append(i)
        return a