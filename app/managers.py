import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.sqlite")
        self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS actors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL
                    )
                ''')
        self.connection.commit()

    def create(self, first_name:str, last_name:str):
        self.connection.execute(
            f"INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self):
        actor_cursor = self.connection.execute(
            f"SELECT * FROM actors"
        )
        rows = actor_cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]

    def update(self, actor_id:int, first_name:str, last_name:str):
        self.connection.execute(
            f"UPDATE actors SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, actor_id:int):
        self.connection.execute(
            f"DELETE FROM actors WHERE id=?",
            (actor_id,)
        )
        self.connection.commit()
