import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor= conn.cursor()
n= int(input("Enter the number of rows to be inserted: "))
tuple_data= []
for i in range(n):
    id= int(input("Enter the id: "))
    name= input("Enter the name: ")
    age= int(input("Enter the age: "))
    # Append the tuple (name, age) to the end of list
    tuple_data.append((id, name, age))
#Insert the data into the table
query= "Insert into student (id, name, age) values(%s, %s, %s)"
cursor.executemany(query, tuple_data)
#commit the changes to the database
conn.commit()
print(f"{cursor.rowcount} rows inserted successfully")
#close the cursor and connection
cursor.close()
conn.close()
