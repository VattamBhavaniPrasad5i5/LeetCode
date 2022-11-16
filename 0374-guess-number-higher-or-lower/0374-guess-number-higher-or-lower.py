# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        mid=(n+1)//2
        while guess(mid)!=0:
            
            if guess(mid)==1:
                low=mid+1
            elif guess(mid)==-1:
                high=mid-1
                
            mid=(low+high)//2
            
        return mid