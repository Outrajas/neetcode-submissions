class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        have = {}
        l = 0
        ans = ""
        min_len = float('inf')
        formed = 0
        required = len(need)
        
        for r in range(len(s)):
            ch = s[r]
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1
            
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]
                
                left_ch = s[l]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1
        
        return ans