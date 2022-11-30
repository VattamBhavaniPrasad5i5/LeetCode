class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp=[]
        s=set(arr)
        for i in s:
            c=arr.count(i)
            if c in temp:
                return False
            else:
                temp.append(c)
        return True