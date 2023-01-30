class Solution:
    def tribonacci(self, n: int) -> int:
        t={0:0,1:1,2:1}
        for i in range(3,n+1):
            t[i]=t[i-1]+t[i-2]+t[i-3]
        return t[n]
        
        # def tribonacci(n):
        #     if n==0:
        #         return 0
        #     elif n==1:
        #         return 1
        #     elif n==2:
        #         return 1
        #     else:
        #         return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
        # return tribonacci(n)
