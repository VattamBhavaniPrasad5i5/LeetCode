class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance=0
        max_b = 0
        for ch in s:
            if ch == '[':
                
                
                balance+= 1
            else:
                balance-= 1
            
            if balance < 0:
                max_b = max(max_b,-balance)
        return (max_b +1)//2