class Solution:
    def anagram(self, s: str) -> dict:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        return d

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t1 = self.anagram(t)
        l, r = 0, 0
        ans = ""
        min_len = float('inf')
        while r < len(s):
            r += 1
            while all(t1[k] <= self.anagram(s[l:r]).get(k, 0) for k in t1):
                if r - l < min_len:
                    min_len = r - l
                    ans = s[l:r]
                l += 1
        return ans