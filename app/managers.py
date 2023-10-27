import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('cinema.db3')

    def create(self, first_name: str, last_name: str) -> None:
        (self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)))
        self._connection.commit()

    def all(self) -> list[Actor]:
        literary_format_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in literary_format_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name=?"
            "WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id=(?)", (actor_id,)
        )
        self._connection.commit()
