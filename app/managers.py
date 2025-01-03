import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        with self.connection:
            self.connection.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) "
                "VALUES (?, ?)",
                (first_name, last_name)
            )

    def all(self) -> list:
        with self.connection:
            cursor = self.connection.execute(
                f"SELECT * FROM {self.table_name}"
            )
            rows = cursor.fetchall()
            actors = [Actor(id=row[0], first_name=row[1], last_name=row[2])
                      for row in rows]
            return actors

    def update(self, actor: Actor) -> None:
        with self.connection:
            self.connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? WHERE id = ?",
                (actor.first_name, actor.last_name, actor.id)
            )

    def delete(self, delete_id: int) -> None:
        with self.connection:
            self.connection.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (delete_id,)
            )

    def close(self) -> None:
        self.connection.close()
