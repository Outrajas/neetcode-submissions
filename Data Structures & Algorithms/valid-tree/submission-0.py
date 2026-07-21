class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return True
                if dfs(neighbor, node):
                    return True
            return False
        
        if dfs(0, -1):
            return False
        
        return len(visited) == n