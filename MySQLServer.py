#!/usr/bin/python3
"""
MySQLServer.py
Creates the database 'alx_book_store' in your MySQL server.

If the database already exists, the script will not fail.
Prints a success message when created and handles errors gracefully.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (Update credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database safely if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
