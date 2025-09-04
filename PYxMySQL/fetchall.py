import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    port=your_port_number,
    user='root',
    password="",
    database="name_of_database"
)
cursor=conn.cursor()
cursor.execute("select * from student")
print(cursor.fetchall())
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()