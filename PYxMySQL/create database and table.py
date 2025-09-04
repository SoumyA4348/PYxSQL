import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    port=your_port_number,
    user="root",
    password="",
    database="name_of_database"
)
cursor=conn.cursor()
cursor.execute("CREATE TABLE contact (contact_id INT PRIMARY KEY AUTO_INCREMENT, id INT, email VARCHAR(50), phone_number INT(10), FOREIGN KEY (id) REFERENCES info(id))")
cursor.close()
conn.close()