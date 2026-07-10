class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        le = 0
        substr = []
        for i in range(len(s)):
            if s[i] in substr:
                le = max(le, len(substr))
                idx = substr.index(s[i])
                substr = substr[idx + 1:]
            substr.append(s[i])
        return max(le, len(substr))