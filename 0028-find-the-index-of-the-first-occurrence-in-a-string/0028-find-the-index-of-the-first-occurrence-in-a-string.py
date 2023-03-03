class Solution:
    def strStr(self, a: str, b: str) -> int:
        if b in a:
            return a.index(b)
        return -1
        