from cachetools import LFUCache

# Define an LFU cache with a max size of 3 items
cache = LFUCache(maxsize=3)

# Insert items into the cache
cache['a'] = 1
cache['b'] = 2
cache['c'] = 3

# Access items to change their frequency
print(cache['a'])  # Access 'a'
print(cache['b'])  # Access 'b'

# Add a new item, evicting the least frequently used (LFU)
cache['d'] = 4

# 'c' should be evicted since it's the least frequently accessed
print(cache)
