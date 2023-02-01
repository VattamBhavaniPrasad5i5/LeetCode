class Solution:
     def gcdOfStrings(self, str1, str2):
        s1, s2 = str1, str2
        while s2:
            s1, s2 = s2, s1[:len(s1)%len(s2)]

        if s1*(len(str1)//len(s1)) == str1 and s1*(len(str2)//len(s1)) == str2:
            return s1
        return ""
     