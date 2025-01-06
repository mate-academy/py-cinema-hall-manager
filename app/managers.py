import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.cursor = self.connection.cursor()
        self.table_name = "actors"

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        query = "INSERT INTO actors (first_name, last_name) VALUES (?, ?)"
        self.cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        query = "SELECT id, first_name, last_name FROM actors"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2])
                for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        query = "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?"
        self.cursor.execute(query, (first_name, last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        query = "DELETE FROM actors WHERE id = ?"
        self.cursor.execute(query, (actor_id,))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
