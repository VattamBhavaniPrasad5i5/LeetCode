class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=len(board)
        colounm=len(board[0])
        for i in board:
            d=set(i)
            d.remove(".")
            for j in d:
                if i.count(j)>1:
                    return False
        arr=[]
        for i in range(9):
            b=[]
            for j in range(9):
                b.append(board[j][i])
            arr.append(b)
      
        for i in arr:
            d=set(i)
            d.remove(".")
            for j in d:
                if i.count(j)>1:
                    return False
        for row in [3, 6, 9]:
                for col in [3, 6, 9]:
                    line = []
                    for i in range(row - 3, row):
                        for j in range(col - 3, col):
                            line.append(board[i][j])
                    d=set(line)
                    d.remove(".")
                    for t in d:
                        if line.count(t)>1:
                            return False
        return True
        
                    
                
                
            
        