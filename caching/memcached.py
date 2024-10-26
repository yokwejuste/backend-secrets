import memcache

# Connect to Memcached
cache = memcache.Client([('127.0.0.1', 11211)])

def expensive_computation(n):
    # Check if result is cached
    result = cache.get(str(n))
    if result:
        return result
    else:
        result = n * n
        cache.set(str(n), result, time=60) # time in seconds
        return result

# Example usage
print(expensive_computation(5))  # Computed and saved to Memcached
print(expensive_computation(5))  # Retrieved from Memcached cache
