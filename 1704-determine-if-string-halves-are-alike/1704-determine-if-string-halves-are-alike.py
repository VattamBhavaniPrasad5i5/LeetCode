class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        a=s[:l//2]
        b=s[l//2:]
        vo=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        su=0
        for i in list(a):
            if i in vo:
                su+=1
        sm=0
        for i in list(b):
            if i in vo:
                sm+=1
        if su==sm:
            return True
        return False
        