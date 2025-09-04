import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)

cursor=conn.cursor()
cursor.execute("select * from student")
results = cursor.fetchall()
print(results)
    # Now, you can get the count by checking the length of the list
row_count = len(results)

print(f"The number of rows returned is: {row_count}")
cursor.close()
conn.close()