import sqlite3 as sq


with sq.connect("cinema.db3") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS
     actors (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)""")
