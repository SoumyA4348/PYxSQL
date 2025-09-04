from datetime import datetime

import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_databse"
)
cursor= conn.cursor()
user_id= int(input("Enter the id of the record to be updated: "))
cursor.execute("SELECT info.id, info.first_name, info.last_name, info.date_of_birth, contact.email, contact.phone_number FROM info JOIN contact ON contact.id = info.id WHERE info.id=%s", (user_id,))
result= cursor.fetchone()
if result:
    print("Current Record:")
    print(f"ID: {result[0]}, first_name: {result[1]}, last_name: {result[2]}, date_of_birth: {result[3]}, email: {result[4]}, phone_number: {result[5]}")
    new_first_name = input("Enter new first name (leave blank to keep current): ")
    new_last_name = input("Enter new last name (leave blank to keep current): ")
    new_date_of_birth = input("Enter new date of birth (leave blank to keep current): ")
    new_email = input("Enter new email (leave blank to keep current): ")
    new_phone_number = input("Enter new phone number (leave blank to keep current): ")
    # Prepare updated values, keeping current if input is blank
    updated_first_name = new_first_name if new_first_name else result[1]
    updated_last_name = new_last_name if new_last_name else result[2]
    updated_date_of_birth = new_date_of_birth if new_date_of_birth else result[3]
    updated_email = new_email if new_email else result[4]
    updated_phone_number = new_phone_number if new_phone_number else result[5]

    # Calculate age if date_of_birth is being updated or provided
    dob_to_check = updated_date_of_birth
    try:
        dob_date = datetime.strptime(str(dob_to_check), "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        if age < 18:
            print("Error: Age must be 18 years or above. Update aborted.")
            cursor.close()
            conn.close()
            exit()
    except ValueError:
        print("Error: Invalid date format for date_of_birth. Use YYYY-MM-DD.")
        cursor.close()
        conn.close()
        exit()

    update_query = """
        UPDATE info
        JOIN contact ON contact.id = info.id
        SET
            info.first_name = %s,
            info.last_name = %s,
            info.date_of_birth = %s,
            contact.email = %s,
            contact.phone_number = %s
        WHERE info.id = %s
    """
    update_data = (
        updated_first_name,
        updated_last_name,
        updated_date_of_birth,
        updated_email,
        updated_phone_number,
        user_id
    )
    cursor.execute(update_query, update_data)
    conn.commit()
    print("Record updated successfully.")
    cursor.close()

    conn.close()
