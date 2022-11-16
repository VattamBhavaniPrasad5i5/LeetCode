class Solution:
    """def minimumTotal(self, triangle: List[List[int]]) -> int:
        su=0
        a=min(triangle[0])
        ind=triangle[0].index(a)
        su=a
        print(a,ind)
        for i in triangle[1:]:
            
            su+=min(i[ind:ind+2])
            ind=triangle.index(min(i[ind:ind+2])) or triangle.index(min(i[ind:ind+1]))
        return su"""
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]