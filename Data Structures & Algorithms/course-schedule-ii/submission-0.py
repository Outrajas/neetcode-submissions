class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        
        state = [0] * numCourses
        order = []
        
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order[::-1]