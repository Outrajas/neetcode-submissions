class Solution:
    def isPalindrome(self, s: str) -> bool:
        si = ''.join(ch for ch in s.lower() if ch.isalnum())
        n = len(si)
        count = 0
        for i in range(n):
            if si[i] == si[n - i - 1]:
                count += 1
        if count == n:
            return True
        return False