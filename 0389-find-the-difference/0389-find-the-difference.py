class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i in s:
                t=t.replace(i,"",1)
                s=s.replace(i,"",1)
            else:
                return i