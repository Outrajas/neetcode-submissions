class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([(src, 0)])  # (node, cost)
        stops = 0
        
        while q and stops <= k:
            for _ in range(len(q)):
                node, cost = q.popleft()
                for neighbor, price in adj[node]:
                    if cost + price < dist[neighbor]:
                        dist[neighbor] = cost + price
                        q.append((neighbor, dist[neighbor]))
            stops += 1
        
        return dist[dst] if dist[dst] != float('inf') else -1