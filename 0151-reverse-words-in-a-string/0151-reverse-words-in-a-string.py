class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split(" "))
        s=s[::-1]
        print(s)
        for i in range(s.count('')):
            s.remove('')
        print(s)
        return ' '.join(s)