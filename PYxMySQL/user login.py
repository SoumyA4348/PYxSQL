import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor = conn.cursor()
rows=cursor.rowcount
username=input("Enter username: ")
password=input("Enter password: ")
credentials = (username, password)
query="""INSERT INTO login (username, password)
        VALUES ( %s, %s)
"""
cursor.execute(query, credentials)

if cursor.rowcount > rows:
    print("Login successful")
else:
    print("Login failed")
conn.commit()
cursor.close()
conn.close()