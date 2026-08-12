# PYxSQL

A Python + MySQL project demonstrating end-to-end database operations: table creation, CRUD, relational queries, authentication, and automated calculations.

## Features

- Create databases and tables (with foreign key relationships)
- Insert, update, and delete records
- CRUD via user input
- SQL JOIN queries across related tables
- Login / credential verification workflow
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

## Tech Stack

- Python, mysql-connector-python, python-dotenv

Originally built as a series of standalone Python-MySQL scripts to learn raw SQL operations.
