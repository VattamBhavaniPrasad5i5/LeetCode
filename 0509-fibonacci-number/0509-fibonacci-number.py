class Solution:
    def fib(self, n: int) -> int:
        # if n == 0 or n==1:
        #     return n
        # fib1, fib2 = 0, 1
        # for x in range(2, n+1):
        #     fib1, fib2 = fib2, fib1 + fib2
        # return fib2
        # if n==1 or n==0:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)