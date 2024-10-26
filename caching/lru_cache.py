from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(n):
    print(f"Computing {n}...")
    return n * n

# Example usage
print(expensive_computation(5))  # Computed and cached
print(expensive_computation(5))  # Retrieved from cache
