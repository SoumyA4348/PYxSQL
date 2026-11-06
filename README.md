# PYxSQL

A Python + MySQL project demonstrating end-to-end database operations: table creation, CRUD, relational queries, authentication, and automated calculations.

## Features

- Create databases and tables (with foreign key relationships)
- Insert, update, and delete records
- CRUD via user input
- SQL JOIN queries across related tables
- Registration and login with salted scrypt password hashes (`auth.py`; no plaintext passwords stored)
- Auto-calculate averages with aggregate functions

## Setup

1. Install dependencies:
   ```bash
   pip install mysql-connector-python python-dotenv
   ```

2. Create a `.env` file:
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=pyxsql_demo
   ```

3. Run the demo:
   ```bash
   python main.py
   ```

This creates the database, tables, inserts sample data, runs updates/deletes, and prints results.

## Schema

```
info(id PK, name, age, email UNIQUE)
contact(contact_id PK, id FK -> info.id ON DELETE CASCADE, phone_number)
login(id PK, username UNIQUE, password_hash)
```

Each table is in 3NF: every non-key column depends only on its table's primary key. One person (`info`) can have many `contact` rows, and deleting a person removes their contacts.

All queries use parameterized `%s` placeholders, and every write is committed or rolled back as one transaction.

## Tests

```bash
pip install -r requirements.txt
pytest
```

The tests mock the database connection, so they run without a MySQL server.

## Tech Stack

- Python, mysql-connector-python, python-dotenv

Originally built as a series of standalone Python-MySQL scripts to learn raw SQL operations.
