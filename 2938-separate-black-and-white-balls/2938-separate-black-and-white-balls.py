class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = black = 0
        for c in s:
            if c == '1':
                black += 1
            else:
                res += black

        return res
        