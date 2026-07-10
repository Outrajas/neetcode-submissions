class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
                continue
            
            if not stack:
                return False

            if not stack.pop() + c in ('()','{}', '[]'):
                return False

        return stack == []