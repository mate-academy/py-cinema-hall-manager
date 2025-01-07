import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> int:
        cursor = self.connection.execute(
            """INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)""",
            (first_name, last_name),
        )
        return cursor.lastrowid

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(
            """SELECT *
            FROM actors"""
        )
        return [
            Actor(id=row[0],
                  first_name=row[1],
                  last_name=row[2])
            for row in cursor.fetchall()
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            """UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?""",
            (first_name, last_name, actor_id),
        )

    def delete(self, actor_id: int) -> None:
        self.connection.execute(
            """DELETE FROM actors
            WHERE id = ?""",
            (actor_id,)
        )
