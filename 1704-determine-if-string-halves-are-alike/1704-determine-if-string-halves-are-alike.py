class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        a=s[:l//2]
        b=s[l//2:]
        #ACM
        vo=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        su=0
        sm=0
        for i in range(l//2):
            if a[i] in vo:
                su+=1
            if b[i] in vo:
                sm+=1
        if su==sm:
            return True
        return False
        