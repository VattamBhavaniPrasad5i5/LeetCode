class Solution:
    def dfs(self, i, group):
        if i in self.group_mapping and group != self.group_mapping[i]:   # Check if there is a conflict
            return False                                                 # between given group and existing group
        self.group_mapping[i] = group
        if i not in self.visited:
            self.visited.add(i)
            for dis in self.graph[i]:                                    # DFS for each dislike node recursively
                if not self.dfs(dis, not group): return False            # Assign contrary group to dislike node
        return True    
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        self.visited, self.group_mapping = set(), {}
        for (u, v) in dislikes:                                          # Create graph 
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, N+1):                                          # DFS until eror
            if i not in self.visited:                                    # We don't want to revisit since it's DFS
                if not self.dfs(i, True):                                # If conflict occurs during DFS, return False
                    return False
        return True