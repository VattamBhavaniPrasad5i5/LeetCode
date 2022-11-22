class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m,n = len(maze),len(maze[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque([entrance])
        
        ### Using extra space to keep track of the visited positions.
        visited = {tuple(entrance)}
        
        ### Use steps to keep track of the level of the BFS.
        steps = 0
        while q:
            
            ### Since we are tracking the steps using a variable, 
            ### we need to pop all elements at each level, then increase the steps.
            for _ in range(len(q)):
                xo,yo = q.popleft()
                if (0 in [xo,yo] or xo==m-1 or yo==n-1) and [xo,yo]!=entrance:
                    return steps
                for xn,yn in directions:
                    x,y = xo+xn,yo+yn
                    ### Check if the new position has been visited or not., and only go into the unvisited ones.
                    if 0<=x<m and 0<=y<n and maze[x][y]=='.' and (x,y) not in visited:
                        visited.add((x,y))
                        q.append([x,y])
            ### Increase the steps since we finished one level.
            steps += 1
        
        return -1