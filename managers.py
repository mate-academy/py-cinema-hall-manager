import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS actors
                     (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)''')

    def create(self, first_name, last_name):
        self.cursor.execute("INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
                            (first_name, last_name))
        self.conn.commit()

    def all(self):
        self.cursor.execute("SELECT * FROM actors")
        return [Actor(*row) for row in self.cursor.fetchall()]

    def update(self, id, first_name, last_name):
        self.cursor.execute("UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
                            (first_name, last_name, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.conn.commit()
