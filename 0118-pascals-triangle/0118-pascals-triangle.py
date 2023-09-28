class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ar=[[1]]
        i=0
        for i in range(numRows-1):
            temp=ar[i]
            #print("temp",temp)
            d=[]
            for j in range(len(temp)-1):
                #print(temp[j]+temp[j+1])
                d.append(temp[j]+temp[j+1])
            s=[temp[0]]+d+[temp[-1]]
            #print(s)
            ar.append(s)
            #print(ar)
            i+=1
        return ar