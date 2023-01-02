class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        w=word.upper()
        w1=word.lower()
        if w==word or w1==word or word[1:]==word[1:].lower():
            return True
        return False