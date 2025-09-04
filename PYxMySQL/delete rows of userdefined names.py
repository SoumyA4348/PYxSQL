import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor= conn.cursor()
n= int(input("Enter the number of records to be deleted: "))
names= []
for i in range(n):
    name= input("Enter the name of the student whose record has to be deleted: ")
    names.append((name,))  # Wrap name in a tuple
query= "delete from student where name = %s"


cursor.executemany(query, names)
conn.commit()