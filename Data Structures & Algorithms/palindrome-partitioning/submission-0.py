class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def dfs(start):
            if start == len(s):
                res.append(part.copy())
                return
            for i in range(start + 1, len(s) + 1):
                sub = s[start:i]
                if sub == sub[::-1]:
                    part.append(sub)
                    dfs(i)
                    part.pop()
        
        dfs(0)
        return res