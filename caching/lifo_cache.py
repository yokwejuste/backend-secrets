from collections import OrderedDict


class LIFOCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        return self.cache.get(key, -1)

    def put(self, key, value):
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=True)  # Remove the last item (LIFO)


# Example usage
cache = LIFOCache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache.cache)

# Add a new item
cache.put("d", 4)
print(cache.cache)  # "c" should be evicted since it's the most recent
