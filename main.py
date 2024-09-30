import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import psycopg2

# splash screen -> player entry
def open_player_entry():
    splash_screen.destroy()

    # Define connection parameters
    connection_params = {
        'dbname': 'photon',
        'user': 'student',
        # 'password': 'student',
        # 'host': 'localhost',
        # 'port': '5432'
    }

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        # Execute a query
        cursor.execute("SELECT version();")

        # Fetch and display the result
        version = cursor.fetchone()
        print(f"Connected to - {version}")

        # Insert sample data
        cursor.execute('''
            INSERT INTO players (id, codename)
            VALUES (%s, %s);
        ''', ('500', 'BhodiLi'))
