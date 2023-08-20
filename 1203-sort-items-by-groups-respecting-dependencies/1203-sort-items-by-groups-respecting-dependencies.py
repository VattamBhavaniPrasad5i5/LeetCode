class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i]==-1:
                group[i]=i+m

        graph0={}
        seen0=[0]*(m+n)
        graph1={}
        seen1=[0]*n

        for i,x in enumerate(beforeItems):
            for j in x:
                if group[j]!=group[i]:
                    graph0.setdefault(group[j],[]).append(group[i])
                    seen0[group[i]]+=1

                graph1.setdefault(j,[]).append(i)
                seen1[i]+=1

        def fn(graph,seen):
            N=len(seen)
            ans=[]
            stack=[k for k in range(N) if seen[k]==0 ]
            while stack:
                n=stack.pop()
                ans.append(n)
                for s in graph.get(n,[]):
                    seen[s]-=1
                    if seen[s]==0:
                        stack.append(s)
            return ans

        top0=fn(graph0,seen0)
        a=len(top0)
        b=len(seen0)       
        if a!=b:
            return []

        top1=fn(graph1,seen1)
        c=len(top1)
        d=len(seen1)
        if c!=d:
            return []
        map0={x:i for i,x in enumerate(top0)}
        map1={x:i for i,x in enumerate(top1)}                                     
        return sorted( range(n),key=lambda x:(map0[group[x]],map1[x]))