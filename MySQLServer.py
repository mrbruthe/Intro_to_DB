#!/usr/bin/python3
"""
MySQLServer.py
Creates the database 'alx_book_store' in your MySQL server.

If the database already exists, the script will not fail.
It prints a success message when created and handles all connection errors gracefully.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust user, password, and host as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # <-- replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL server or create database.\n{e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional message
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
