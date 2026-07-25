class CountSquares:
    def __init__(self):
        self.pts = {}
    
    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.pts[p] = self.pts.get(p, 0) + 1
    
    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for (px, py), cnt in self.pts.items():
            if abs(px - x) != abs(py - y) or px == x:
                continue
            count += cnt * self.pts.get((x, py), 0) * self.pts.get((px, y), 0)
        return count