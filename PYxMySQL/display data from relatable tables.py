import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor= conn.cursor()

"""
# to fetch data from specific user id
user_id= int(input("Enter the id of the record to be displayed: "))
cursor.execute("select info*, contact.contact_id, contact.email, contact.phone_number from info join contact on contact.id=info.id where info.id=%s", (user_id,))
"""

last_name= input("Enter the last name of the record to be displayed: ")
cursor.execute(
    "select info.*, contact.contact_id, contact.email, contact.phone_number from info join contact on contact.id=info.id where info.last_name like %s",
    (last_name + '%',)
)

result= cursor.fetchall()
if result:
    for row in result:
        print("Record:")
        print(f"ID: {row[0]}, first_name: {row[1]}, last_name: {row[2]}, date_of_birth: {row[3]}, contact_id: {row[4]}, email: {row[5]}, phone_number: {row[6]}")
else:
    print("No records found for the given last name.")

cursor.close()
conn.close()
