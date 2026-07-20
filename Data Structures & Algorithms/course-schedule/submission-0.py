class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        
        state = [0] * numCourses 
        
        def has_cycle(course):
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False
            state[course] = 1
            for neighbor in adj[course]:
                if has_cycle(neighbor):
                    return True
            state[course] = 2
            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True