class Solution:
    def sortArray(self, num: List[int]) -> List[int]:
        if len(num)>1:
            mid=len(num)//2
            l=num[:mid]
            r=num[mid:]
            self.sortArray(l)
            self.sortArray(r)
            i=j=k=0
            while i<len(l) and j<len(r):
                if l[i]<=r[j]:
                    num[k]=l[i]
                    i+=1
                else:
                    num[k]=r[j]
                    j+=1
                k+=1
            while i<len(l):
                num[k]=l[i]
                i+=1
                k+=1
            while j<len(r):
                num[k]=r[j]
                j+=1
                k+=1
            return num
        return num