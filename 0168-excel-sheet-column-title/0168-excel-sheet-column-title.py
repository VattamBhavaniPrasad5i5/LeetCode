# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         n=columnNumber
#         a=""
#         b="ZABCDEFGHIJKLMNOPQRSTUVWXY"
#         while n>26:
#             print(n)
#             a+=b[n%26]
#             n=(n//26)
#             print(n)
#         a+=b[(n%26)]
#         print(a)
#         return a[::-1]
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:       
        ans=""        
        while columnNumber>0:
            c=chr(ord('A')+(columnNumber-1)%26)
            ans=c+ans
            columnNumber=(columnNumber-1)//26            
        return ans   
            