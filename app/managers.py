import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")

    def all(self) -> list[Actor]:
        literary_format_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )

        return [Actor(*row) for row in literary_format_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def update(self, primary_key_: int,
               first_name: str,
               last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, primary_key_)
        )
        self._connection.commit()

    def delete(self, primary_key_: int) -> None:
        self._connection.execute(
            "DELETE FROM actors "
            "WHERE id = ?",
            (primary_key_,)
        )
        self._connection.commit()
