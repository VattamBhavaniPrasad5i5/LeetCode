class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        for i in word1:
            w1+=i
        w2=""
        for i in word2:
            w2+=i
        if w1==w2:
            return True
        return False