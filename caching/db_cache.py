import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('cache.db')
cursor = conn.cursor()

# Create a cache table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cache (
        key TEXT PRIMARY KEY,
        value TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()


# Function to get cached value
def get_from_cache(key):
    cursor.execute("SELECT value FROM cache WHERE key = ?", (key,))
    result = cursor.fetchone()
    return result[0] if result else None


def set_in_cache(key, value):
    cursor.execute("INSERT OR REPLACE INTO cache (key, value) VALUES (?, ?)", (key, value))
    conn.commit()


# Example usage
set_in_cache("username", "JohnDoe")
print(get_from_cache("username"))  # If all is well it should return "JohnDoe"
