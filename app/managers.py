import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.connection.row_factory = sqlite3.Row

    def create(self, first_name: str, last_name: str) -> Actor:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
        return Actor(
            id=cursor.lastrowid, first_name=first_name, last_name=last_name
        )

    def all(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM actors")
        rows = cursor.fetchall()
        return [
            Actor(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"]
            ) for row in rows
        ]

    def update(
            self,
            actor_id: int,
            first_name: str = None,
            last_name: str = None
    ) -> None:
        cursor = self.connection.cursor()
        if first_name:
            cursor.execute(
                "UPDATE actors SET first_name = ? WHERE id = ?",
                (first_name, actor_id)
            )
        if last_name:
            cursor.execute(
                "UPDATE actors SET last_name = ? WHERE id = ?",
                (last_name, actor_id)
            )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
