import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.conn = sqlite3.connect("cinema.sqlite")
    
    def create(self, first_name: str, last_name: str):
        self.conn.execute("INSERT INTO actors (first_name, last_name)"
                       "VALUES (?, ?)",
                       (first_name, last_name))
        self.conn.commit()
        self.conn.close()

    def all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM actors")
        return [Actor(*row) for row in cursor.fetchall()]
    
    def update(self, actor):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE actors SET name = ?, age = ? WHERE id = ?", (actor.name, actor.age, actor.id))
        self.conn.commit()
        self.conn.close()

    def delete(self, actor):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (actor.id,))
        self.conn.commit()
        self.conn.close()