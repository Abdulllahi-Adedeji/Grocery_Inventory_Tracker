import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="        ",
    database="grocery_inventory"
)

cursor = conn.cursor()

print("Connected to MySQL database!")