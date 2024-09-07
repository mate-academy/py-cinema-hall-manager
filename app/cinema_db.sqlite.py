import sqlite3

conn = sqlite3.connect("cinema_db.sqlite")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS actors ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "first_name VARCHAR(255) NOT NULL, "
    "last_name VARCHAR(255) NOT NULL)"
)
conn.commit()
conn.close()
