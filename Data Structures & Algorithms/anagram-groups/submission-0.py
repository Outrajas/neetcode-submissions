class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - 97] += 1
            groups[tuple(key)].append(s)
        return list(groups.values())