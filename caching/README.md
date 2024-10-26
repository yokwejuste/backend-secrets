[Back to Main README](../README.md)

# Caching

This folder contains various caching implementations in Python, each suited for different use cases, from in-memory caching to file-based and distributed caching solutions.

## Contents

- [Redis Cache](#redis-cache)
- [Database Cache (SQLite)](#database-cache-sqlite)
- [Disk-Based Cache](#disk-based-cache)
- [FIFO Cache](#fifo-cache)
- [LIFO Cache](#lifo-cache)
- [LFU Cache](#lfu-cache)
- [LRU Cache](#lru-cache)
- [Memcached](#memcached)

---

### Redis Cache

**Redis Cache** is a high-performance distributed caching solution, often used for real-time applications.

- **Files**:
  - `main.py`: Example of connecting to Redis and using it for caching.
  - `redis.conf`: Configuration file for Redis server.

- **Setup**:
  1. Install the Redis Python client: `pip install redis`.
  2. Configure the `redis.conf` file as needed.
  3. Start Redis server and run `main.py`.

- **Example Usage**:
  ```python
  from redis_cache.main import cache_set, cache_get
  cache_set("key", "value")
  print(cache_get("key"))
  ```

---

### Database Cache (SQLite)

**Database Cache** uses SQLite to store cache data persistently, making it useful for caching small datasets that need to survive restarts.

- **File**: `db_cache.py`
- **Setup**:
  1. No additional setup required if Python's SQLite library is available.
  
- **Example Usage**:
  ```python
  from db_cache import get_from_cache, set_in_cache
  set_in_cache("user_id", "12345")
  print(get_from_cache("user_id"))
  ```

---

### Disk-Based Cache

**Disk-Based Cache** uses file storage for caching, making it persistent across application restarts.

- **File**: `disk_cache.py`
- **Setup**:
  1. Install `diskcache`: `pip install diskcache`.

- **Example Usage**:
  ```python
  from disk_cache import disk_cache_set, disk_cache_get
  disk_cache_set("username", "admin")
  print(disk_cache_get("username"))
  ```

---

### FIFO Cache

**FIFO (First-In, First-Out) Cache** evicts the oldest cache entries first, making it ideal for cases where the order of data matters.

- **File**: `fifo_cache.py`

- **Example Usage**:
  ```python
  from fifo_cache import FIFOCache
  cache = FIFOCache(3)
  cache.put("a", 1)
  cache.put("b", 2)
  cache.put("c", 3)
  cache.put("d", 4)  # "a" is evicted
  ```

---

### LIFO Cache

**LIFO (Last-In, First-Out) Cache** evicts the most recently added item first, useful for stack-like data storage.

- **File**: `lifo_cache.py`

- **Example Usage**:
  ```python
  from lifo_cache import LIFOCache
  cache = LIFOCache(3)
  cache.put("x", 10)
  cache.put("y", 20)
  cache.put("z", 30)
  cache.put("a", 40)  # "z" is evicted
  ```

---

### LFU Cache

**LFU (Least Frequently Used) Cache** evicts the least accessed items, suitable for scenarios with infrequent access patterns.

- **File**: `lfu_cache.py`

- **Example Usage**:
  ```python
  from lfu_cache import LFUCache
  cache = LFUCache(3)
  cache.put("apple", 1)
  cache.put("banana", 2)
  cache.get("apple")
  cache.put("cherry", 3)
  cache.put("date", 4)  # "banana" is evicted
  ```

---

### LRU Cache

**LRU (Least Recently Used) Cache** removes the least recently accessed items, making it suitable for applications where data accessed frequently is retained.

- **File**: `lru_cache.py`

- **Example Usage**:
  ```python
  from lru_cache import LRUCache
  cache = LRUCache(3)
  cache.put("key1", "value1")
  cache.put("key2", "value2")
  cache.get("key1")
  cache.put("key3", "value3")
  cache.put("key4", "value4")  # "key2" is evicted
  ```

---

### Memcached

**Memcached** is an in-memory caching solution designed for distributed systems.

- **File**: `memcached.py`
- **Setup**:
  1. Install `python-memcached`: `pip install python-memcached`.
  2. Start a Memcached server.

- **Example Usage**:
  ```python
  from memcached import memcached_set, memcached_get
  memcached_set("session_id", "ABC123")
  print(memcached_get("session_id"))
  ```

---

## How to Use

1. Clone the repository and navigate to the `caching` folder.
2. Install any required dependencies as mentioned in each section.
3. Configure and run each script as needed for the caching strategy you want to implement.

## Contributing

Contributions are welcome! If you’d like to add more caching techniques or improve existing ones, please submit a pull request with a detailed description of your changes.
