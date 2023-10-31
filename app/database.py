import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()


cursor.execute(
    """CREATE TABLE IF NOT EXISTS actors (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255) 
    )"""
)

conn.commit()
conn.close()
