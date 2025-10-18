# A simple python script that creates the database alx_book_store

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("MYSQL_HOST")
user=os.getenv("MYSQL_USER")
password=os.getenv("MYSQL_PASSWORD")
database=os.getenv("MYSQL_DATABASE")

print("🔍 Checking environment variables...")
print(f"Host: {host}")
print(f"User: {user}")
print(f"Password: {'*' * len(password) if password else None}")
print(f"Database: {database}")

try:
    print("Connecting to mysql")
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully.")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed.")