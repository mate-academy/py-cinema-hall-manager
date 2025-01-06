import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str = "cinema.sqlite3") -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.initialize_db()

    def initialize_db(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
        actor_id = self.cursor.lastrowid
        return Actor(actor_id, first_name, last_name)

    def all(self) -> list[Actor]:
        self.cursor.execute(
            "SELECT id, first_name, last_name FROM actors"
        )
        rows = self.cursor.fetchall()
        return [
            Actor(id=row[0],
                  first_name=row[1],
                  last_name=row[2])
            for row in rows
        ]

    def update(self,
               actor_id: int,
               first_name: str = None,
               last_name: str = None) -> None:
        if first_name:
            self.cursor.execute(
                "UPDATE actors SET first_name = ? WHERE id = ?",
                (first_name, actor_id)
            )
        if last_name:
            self.cursor.execute(
                "UPDATE actors SET last_name = ? WHERE id = ?",
                (last_name, actor_id)
            )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
