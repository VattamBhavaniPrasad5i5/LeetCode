class Solution:
    def hammingWeight(self, n: int) -> int:
        s=0
        n=int(bin(n)[2:])
        while(n>0):
            if n%10==1:
                s+=1
            n=n//10
        return s
        
        