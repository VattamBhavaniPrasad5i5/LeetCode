class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in s:
            if "AB" or "CD" in s:
                s =s.replace("AB","")
                s =s.replace("CD","")
                # print(s)
            else:
                return len(s)
        return len(s)