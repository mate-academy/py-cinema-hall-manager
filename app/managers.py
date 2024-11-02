import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in cursor]

    def update(self, actor_id: int,
               first_name: str = None,
               last_name: str = None) -> Actor:
        fields = []
        values = []

        if first_name:
            fields.append("first_name = ?")
            values.append(first_name)

        if last_name:
            fields.append("last_name = ?")
            values.append(last_name)

        values.append(actor_id)
        self._connection.execute(
            f"UPDATE actors SET {', '.join(fields)} WHERE id = ?",
            values
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
