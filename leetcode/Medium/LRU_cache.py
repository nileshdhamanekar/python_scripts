# https://leetcode.com/problems/lru-cache/
# No resource. Solved on my own :-) May not be the best solution though

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.count = 0
        self.queue = list()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            value = self.cache[key]
            if key in self.queue:
                self.queue.remove(key)
            self.queue.insert(0, key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.queue.remove(key)
        if len(self.queue) >= self.capacity:
            deleted_item = self.queue.pop()
            del self.cache[deleted_item]
        self.cache[key] = value
        self.queue.insert(0, key)