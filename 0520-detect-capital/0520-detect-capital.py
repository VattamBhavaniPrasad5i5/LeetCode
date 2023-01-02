class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        w=word.upper()
        w1=word.lower()
        w2=word.capitalize()
        if w==word or w1==word or w2==word:
            return True
        return False