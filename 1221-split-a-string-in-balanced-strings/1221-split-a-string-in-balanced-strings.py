# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         sta=[]
#         f=0
#         c=0
#         for i in s:
#             if i=='R':
#                 sta.append(i)
#                 print(sta)
#                 f=1
#             elif i=="L" and f==1:
#                 sta.pop()
#             if f==1 and len(sta)==0:
#                 c+=1
#                 f=0
#         if len(sta)==len(s)//2:
#             return 1
#         return c
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = prefix = 0
        for c in s: 
            prefix += 1 if c == "R" else -1
            if not prefix: ans += 1
        return ans 