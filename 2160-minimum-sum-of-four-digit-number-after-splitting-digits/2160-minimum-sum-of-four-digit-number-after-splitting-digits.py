class Solution:
    def minimumSum(self, num: int) -> int:
        a=[]
        while num:
            r=num%10
            a.append(r)
            num=num//10
        a.sort()
        return (a[0]*10)+(a[1]*10)+a[2]+a[3]