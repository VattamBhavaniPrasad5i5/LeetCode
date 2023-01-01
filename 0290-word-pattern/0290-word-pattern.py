class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a={}
        s=list(s.split(" "))
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in a:
                if a[pattern[i]]!=s[i]:
                    return False
                
            else:
                if s[i] not in a.values():
                    a[pattern[i]]=s[i]
                else:
                    return False
        return True
            