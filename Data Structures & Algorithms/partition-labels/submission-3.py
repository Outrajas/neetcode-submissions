class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        total = Counter(s)
        window = Counter()
        res = []
        start = 0
        
        for i, c in enumerate(s):
            window[c] += 1
            if all(window[ch] == total[ch] for ch in window):
                res.append(i - start + 1)
                start = i + 1
                window.clear()
        
        return res