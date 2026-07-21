class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        T = '^#' + '#'.join(s) + '#$ '
        n = len(T)
        P = [0] * n
        C = R = 0
        
        for i in range(1, n - 1):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])
            
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            if i + P[i] > R:
                C = i
                R = i + P[i]
        
        max_len = max(P)
        center = P.index(max_len)
        start = (center - max_len) // 2
        return s[start: start + max_len]