class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=list(a),list(b)
        d=0
        a,b=a[::-1],b[::-1]
        print(a,b)
        for i in range(len(a)):
            d+=(2**i)*int(a[i])
        c=0
        for i in range(len(b)):
            c+=(2**i)*int(b[i])
        print(c,d)
        return bin(d+c)[2:]
        
            
        