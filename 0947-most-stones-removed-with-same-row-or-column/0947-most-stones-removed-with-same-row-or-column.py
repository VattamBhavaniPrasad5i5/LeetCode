"""class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        a=[]
        b=[]
        for i in stones[::-1]:
            a.append(i[0])
            b.append(i[1])
        print(a)
        print(b)
        re=0
        for i in range(len(stones)):
            if a[i] in a[i+1:]:
                re+=1
                continue
            elif b[i] in b[i+1:]:
                re+=1
                continue
            else:
                continue
        return re"""
class Solution(object):
    def removeStones(self, stones):
        X, Y = {}, {}
        uf = [i for i in range(len(stones))]
        
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        for i, coord in enumerate(stones):
            x, y = coord
            if x not in X:
                X[x] = i
            if y not in Y:
                Y[y] = i
            uf[find(Y[y])] = uf[find(X[x])] = find(i)
            
        return len(stones) - len(set([find(i) for i in range(len(stones))]))