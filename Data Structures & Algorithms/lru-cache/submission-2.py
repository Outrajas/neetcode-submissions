class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.order = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.order[key] = self.order.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order[key] = self.order.pop(key)
            return
        if len(self.cache) == self.cap:
            lru = next(iter(self.order))
            del self.cache[lru]
            del self.order[lru]
        self.cache[key] = value
        self.order[key] = None