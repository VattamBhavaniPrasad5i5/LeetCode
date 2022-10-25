class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """a=""
        for i in word1:
            a+=i
        b=""
        for i in word2:
            b+=i
        if a==b:
            return True
        return False
        """
        print("".join(word1))
        return "".join(word1)=="".join(word2)
