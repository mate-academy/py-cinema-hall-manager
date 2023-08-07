import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")

    def all(self) -> None:
        actors_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )

        return [Actor(*line) for line in actors_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors(first_name, last_name) VALUES(?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_update: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_update)
        )
        self._connection.commit()

    def delete(self, id_delete: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_delete,)
        )
        self._connection.commit()
