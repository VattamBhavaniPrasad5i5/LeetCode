class Solution:
    def climbStairs(self, n: int) -> int:
        f1,f2=1,1
        if n==0 or n==1:
            return n
        for i in range(2,n+1):
            f1,f2=f2,f1+f2
        return f2