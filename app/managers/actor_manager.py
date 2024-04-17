import sqlite3

from typing import List

from app.models.actor import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/cinema.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS actors (
                                id INTEGER PRIMARY KEY,
                                first_name TEXT,
                                last_name TEXT
                                )""")
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> List[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "UPDATE actors SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id=?", (actor_id,))
        self.connection.commit()
