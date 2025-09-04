import datetime

import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor=conn.cursor()
print("Login portal")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
email = input("Enter your email: ")
phone_number = int(input("Enter your phone number: "))
credentials = (first_name, last_name, date_of_birth)

# Calculate age in years
dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
today = datetime.date.today()
age_years = today.year - dob.year


if age_years < 18:
    print("You must be at least 18 years old to register.")


else:
    cursor.execute("INSERT INTO info (first_name, last_name, date_of_birth) VALUES (%s, %s, %s)", 
                   credentials)
    last_id = cursor.lastrowid
    print(f"Your user ID is: {last_id}")
    cursor.execute("INSERT INTO contact (id, email, phone_number) VALUES (%s, %s, %s)", 
                   (last_id, email, phone_number))
    print("Registration successful!")
    conn.commit()

cursor.close()
conn.close()
