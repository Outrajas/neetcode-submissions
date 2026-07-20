class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        
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
        
        for a, b in edges:
            visited = set()
            adj[a].append(b)
            adj[b].append(a)
            if dfs(a, -1):
                return [a, b]
        return []