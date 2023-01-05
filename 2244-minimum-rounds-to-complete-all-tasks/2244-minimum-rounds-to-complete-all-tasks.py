class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic={}
        re=0
        flag=0
        for i in range(len(tasks)):
            if tasks[i] in dic:
                dic[tasks[i]]+=1
            else:
                dic[tasks[i]]=1
        """ p=0
        print(dic)
        for i in dic:
            #print(dic[i],i)
            if dic[i]==2 or dic[i]==3:
                re+=1
            elif dic[i]==1:
                flag=1
                break
            else:
                while dic[i]>0:
                    
                    re+=1
                    #print(dic[i])
                    dic[i]=dic[i]-3
                    #print(dic[i])
        if flag==0:
            return re
        else:
            return -1
                """
        ans=0
        for i in dic.values():
            if i==1:
                return -1
            ans+=(i//3)+(i%3!=0)
        return ans
                