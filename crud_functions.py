import sqlite3
import os


def initiate_db():
    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
            )
        ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

def populate_products():
    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()
    products = [
        ('Product1', 'Description1', 100),
        ('Product2', 'Description2', 200),
        ('Product3', 'Description3', 300),
        ('Product4', 'Description4', 400)
    ]
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    connection.commit()
    connection.close()


