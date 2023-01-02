import time
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s_time=time.time()
        w=word.upper()
        w1=word.lower()
        w2=word.capitalize()
        if w==word or w1==word or w2==word:
             endtime=time.time()
             print(endtime-s_time)
             return True
        endtime=time.time()
        print(endtime-s_time)
        return False