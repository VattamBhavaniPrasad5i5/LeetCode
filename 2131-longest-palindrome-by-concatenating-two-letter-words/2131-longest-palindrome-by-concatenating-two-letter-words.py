class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        l = Counter(words)
        p_len = 0
        mid = 0
        for word in l.keys():
            if word[0] == word[1]:
                if l[word]%2 == 0:
                    p_len += l[word]
                else:
                    p_len += l[word]-1
                    mid = 1
            elif word[::-1] in l:
                p_len += min(l[word], l[word[::-1]])
        return (p_len + mid) * 2
            