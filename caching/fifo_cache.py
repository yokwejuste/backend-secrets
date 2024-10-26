from collections import OrderedDict

class FIFOCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        return self.cache.get(key, -1)

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the first item (FIFO)

# Example usage
cache = FIFOCache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache.cache)

# Add a new item
cache.put("d", 4)
print(cache.cache)  # "a" should be evicted since it's the oldest
