class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        print(row,col)
        for i in range(m):
            for j in range(n):
                if i in row:
                    matrix[i][j]=0
                if j in col:
                    matrix[i][j]=0
        