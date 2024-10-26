[Back to Main README](../README.md)

# Databases

This folder contains Python scripts for connecting to and interacting with various types of databases, each suited for different use cases and data structures. Each script provides functions for common database operations such as connecting, querying, inserting, updating, and deleting records.

## Contents

- [MySQL Database](#mysql-database)
- [PostgreSQL Database](#postgresql-database)
- [SQLite Database](#sqlite-database)
- [MongoDB Database](#mongodb-database)
- [Redis Database](#redis-database)
- [Cassandra Database](#cassandra-database)
- [Neo4j Database](#neo4j-database)
- [Elasticsearch](#elasticsearch)
- [Amazon Aurora](#amazon-aurora)

---

### MySQL Database

**MySQL** is a widely used open-source relational database that’s known for its reliability and ease of use.

- **File**: `mysql_database.py`
- **Setup**:
  1. Install MySQL client library: `pip install mysql-connector-python`.
  2. Configure MySQL credentials.

- **Example Usage**:
  ```python
  from mysql_database import connect_to_mysql, execute_query
  connection = connect_to_mysql()
  execute_query(connection, "SELECT * FROM my_table")
  ```

---

### PostgreSQL Database

**PostgreSQL** is a powerful, open-source relational database system known for its robustness and support for complex queries.

- **File**: `postgresql_database.py`
- **Setup**:
  1. Install PostgreSQL client library: `pip install psycopg2`.
  2. Configure PostgreSQL credentials.

- **Example Usage**:
  ```python
  from postgresql_database import connect_to_postgresql, execute_query
  connection = connect_to_postgresql()
  execute_query(connection, "SELECT * FROM my_table")
  ```

---

### SQLite Database

**SQLite** is a lightweight, file-based relational database often used for small-scale applications and testing.

- **File**: `sqlite_database.py`
- **Setup**:
  - No additional installation is required as SQLite is included with Python.

- **Example Usage**:
  ```python
  from sqlite_database import connect_to_sqlite, execute_query
  connection = connect_to_sqlite("database.db")
  execute_query(connection, "SELECT * FROM my_table")
  ```

---

### MongoDB Database

**MongoDB** is a NoSQL database known for its flexibility and scalability, making it suitable for large datasets and unstructured data.

- **File**: `mongodb_database.py`
- **Setup**:
  1. Install MongoDB client library: `pip install pymongo`.
  2. Configure MongoDB connection details.

- **Example Usage**:
  ```python
  from mongodb_database import connect_to_mongodb, insert_document
  db = connect_to_mongodb("my_database")
  insert_document(db, "my_collection", {"name": "Alice", "age": 30})
  ```

---

### Redis Database

**Redis** is an in-memory key-value store, often used for caching and real-time analytics.

- **File**: `redis_database.py`
- **Setup**:
  1. Install Redis client library: `pip install redis`.
  2. Configure Redis connection settings.

- **Example Usage**:
  ```python
  from redis_database import connect_to_redis, set_key, get_key
  redis_client = connect_to_redis()
  set_key(redis_client, "username", "john_doe")
  print(get_key(redis_client, "username"))
  ```

---

### Cassandra Database

**Cassandra** is a distributed NoSQL database designed to handle large amounts of data across many servers, providing high availability.

- **File**: `cassandra_database.py`
- **Setup**:
  1. Install Cassandra driver: `pip install cassandra-driver`.
  2. Configure Cassandra cluster connection.

- **Example Usage**:
  ```python
  from cassandra_database import connect_to_cassandra, execute_query
  session = connect_to_cassandra()
  execute_query(session, "SELECT * FROM my_table")
  ```

---

### Neo4j Database

**Neo4j** is a graph database that stores data in nodes and relationships, making it suitable for applications involving complex relationships.

- **File**: `neo4j_database.py`
- **Setup**:
  1. Install Neo4j client library: `pip install neo4j`.
  2. Configure Neo4j connection settings.

- **Example Usage**:
  ```python
  from neo4j_database import connect_to_neo4j, execute_cypher_query
  driver = connect_to_neo4j()
  execute_cypher_query(driver, "MATCH (n) RETURN n")
  ```

---

### Elasticsearch

**Elasticsearch** is a distributed search and analytics engine often used for log and text data storage and querying.

- **File**: `elasticsearch_database.py`
- **Setup**:
  1. Install Elasticsearch client: `pip install elasticsearch`.
  2. Configure Elasticsearch connection settings.

- **Example Usage**:
  ```python
  from elasticsearch_database import connect_to_elasticsearch, search_index
  es = connect_to_elasticsearch()
  search_results = search_index(es, "my_index", {"query": {"match_all": {}}})
  ```

---

### Amazon Aurora

**Amazon Aurora** is a MySQL and PostgreSQL-compatible relational database built for the cloud, providing high performance and availability.

- **File**: `aurora_database.py`
- **Setup**:
  1. Install the MySQL or PostgreSQL client library (depending on Aurora's compatibility mode): 
     - For MySQL: `pip install mysql-connector-python`
     - For PostgreSQL: `pip install psycopg2`
  2. Configure Aurora database endpoint, username, password, and database name.

- **Example Usage**:
  ```python
  from aurora_database import connect_to_aurora, execute_query
  connection = connect_to_aurora()
  execute_query(connection, "SELECT * FROM my_table")
  ```

---

## How to Use

1. Clone the repository and navigate to the `databases` folder.
2. Install any required dependencies as mentioned in each section.
3. Configure your database credentials or connection settings for each database type.
4. Use the example code snippets in each script to connect to, query, or manipulate data in the respective database.

## Contributing

Contributions are welcome! If you’d like to add more database types or enhance existing implementations, please submit a pull request with a detailed description of your changes.
