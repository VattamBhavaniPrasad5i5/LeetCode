class Solution:
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start) # update the res
                start = max(start, dic[ch]+1)  # here should be careful, like "abba"
            dic[ch] = i
        return max(res, len(s)-start)