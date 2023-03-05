class Solution:
    def minJumps(self, arr):
        n = len(arr)
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
            
        queue = deque([(0, 0)])
        visited, visited_groups = set(), set()
        
        while queue:
            steps, index = queue.popleft()
            if index == n - 1: return steps
            
            for neib in [index - 1, index + 1]:
                if 0 <= neib < n and neib not in visited:
                    visited.add(neib)
                    queue.append((steps + 1, neib))
            
            if arr[index] not in visited_groups:
                for neib in d[arr[index]]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append((steps + 1, neib))
                visited_groups.add(arr[index])