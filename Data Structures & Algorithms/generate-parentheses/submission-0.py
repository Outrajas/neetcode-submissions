class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(temp, open_count, close_count):
            if len(temp) == 2 * n:
                ans.append(temp)
                return
            if open_count < n:
                backtrack(temp + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(temp + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return ans