import diskcache as dc

cache = dc.Cache('/tmp/my_cache')

def expensive_computation(n):
    if n in cache:
        return cache[n]
    else:
        result = n * n
        cache[n] = result
        return result

# Example usage
print(expensive_computation(5))  # Computed and saved to disk cache
print(expensive_computation(5))  # Retrieved from disk cache
