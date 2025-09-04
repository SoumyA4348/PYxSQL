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
data= cursor.fetchall()

n=cursor.rowcount
#a is the index of the age column in the data
def average_age(a):
    total_age = 0
    for row in data:
        total_age+=row[a]
    print("Average age of students is: ", total_age/n)
for i in range(len(data[0])):
    if isinstance(data[0][i], int):
        average_age(i)
    else:
        print("Column", i, "is not an integer type, skipping average calculation.")
cursor.close()
conn.close()