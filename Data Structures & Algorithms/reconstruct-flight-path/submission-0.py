from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            adj[u].append(v)
        
        path = []
        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            path.append(node)
        
        dfs("JFK")
        return path[::-1]