class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        a={}
        for i in tickets:
            a[i[0]]=[]
            a[i[1]]=[]
        for i in tickets:
            a[i[0]].append(i[1])
        print(a)
        for i in a.values():
            i.sort()
        ans=[]
        def helper(node):
            while a[node]:
                helper(a[node].pop(0))
            ans.append(node)
        helper('JFK')
        return reversed(ans)