import sqlite3

connection = sqlite3.connect("cinema.db3")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    )
""")

connection.commit()
connection.close()
