import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor= conn.cursor()
print("To update the age:")
name= input("Enter the name of the person whose age is to be updated: ")
new_age= int(input("Enter the new age: "))
query= "Update student set age= %s where name= %s"
data= (new_age, name)
cursor.execute(query, data)
conn.commit()
print("Age updated successfully.")
cursor.close()
conn.close()