import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor=conn.cursor()
query = "select * from student"
cursor.execute(query)
data = cursor.fetchall()
n = cursor.rowcount
print("Total number of rows in the table:", n)
total_age = 0
if isinstance(data[0][1], int):
    for row in data:
        total_age += row[1]
    print("Total age of all students:", total_age)
    print("Average age of students:", total_age / n)
else:
    if isinstance(data[0][2], int):
        for row in data:
            total_age += row[2]
        print("Total age of all students:", total_age)
        print("Average age of students:", total_age / n)
    else:
        print("No age data found in the table.")
cursor.close()
conn.close()