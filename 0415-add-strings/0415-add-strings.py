# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         if len(num1)<4300 and len(num2)<4300:
#             num=int(num1)+int(num2)
#         # else:
#         #     if len(num2)>4300:
#         #         return 
#         return str(num)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        i1, i2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry > 0:
            if i1 >= 0:
                carry += ord(num1[i1]) - ord('0')
                i1 -= 1
            if i2 >= 0:
                carry += ord(num2[i2]) - ord('0')
                i2 -= 1
            ans.append(chr(carry % 10 + ord('0')))
            carry //= 10
        return "".join(ans)[::-1]