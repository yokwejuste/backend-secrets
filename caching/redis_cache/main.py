import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

cache = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True,
)

def expensive_computation(n):
    if cache.exists(n):
        return cache.get(n)
    else:
        result = n * n
        cache.set(n, result, ex=60)
        return result

# Example usage
print(expensive_computation(5))  # Computed and saved to Redis
print(expensive_computation(5))  # Retrieved from Redis cache
