class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        le=len(palindrome)
        temp_li=list(palindrome)
        temp=0
        if le==1:
            return ""
        elif len(set(temp_li))==2 and [i for i in temp_li if temp_li.count(i)==1] and temp_li.count('a')!=1:
            temp_li[-1]='b'
        else:
            for i in range(len(temp_li)):
                if temp_li[i]!='a':
                    #print(temp_li[i])
                    temp_li[i]='a'
                    #print(temp_li[i],li)
                    temp=1
                    break
            if temp==0:
                temp_li[-1]='b'
        p=""
        for i in temp_li:
            p+=i
        return p
                    
                    
        
