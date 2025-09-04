import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor=conn.cursor()
# SQL query to calculate the average age of all students
query = "SELECT AVG(age) FROM student"
cursor.execute(query)
result = cursor.fetchone()
print(result)
# Fetching the result
if result[0] is not None:
    average_age=result[0]
    print(f"The average age of all students is: {average_age}")
else:
    print("No students found in the database.")
# Closing the cursor and connection
cursor.close()
conn.close()