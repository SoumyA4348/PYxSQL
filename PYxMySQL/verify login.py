import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor = conn.cursor()
print("To verify your login, please enter your credentials.")
username = input("Enter username: ")
password = input("Enter password: ")
query = """SELECT * FROM login WHERE username = %s AND password = %s"""
credentials = (username, password)
cursor.execute(query, credentials)
result= cursor.fetchall()
if cursor.rowcount > 0:
    print("Login was successful")
else:
    print("No such user found, please try again")
cursor.close()
conn.close()