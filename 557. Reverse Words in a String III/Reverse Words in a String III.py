class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split(" "))
        a=""
        for i in s:
            a+=i[::-1]
            a+=" "
        return a[:-1]
            
