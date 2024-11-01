import sqlite3
from models import Actor
from typing import List


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (
                first_name,
                last_name
            )
        )
        self.conn.commit()
        return Actor(
            id=self.cursor.lastrowid,
            first_name=first_name,
            last_name=last_name
        )

    def all(self) -> List[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"]
            )
            for row in rows
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (
                first_name,
                last_name,
                actor_id
            )
        )
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self.conn.commit()
