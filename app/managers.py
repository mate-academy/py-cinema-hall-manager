import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self._table_name = "actors"

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )

        return [
            Actor(*row) for row in actors_cursor
        ]

    def create(self, _first_name: str, _last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (_first_name, _last_name)
        )
        self._connection.commit()

    def update(self, _id: int, _first_name: str, _last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (_first_name, _last_name, _id)
        )
        self._connection.commit()

    def delete(self, _id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?",
            (_id,)
        )
        self._connection.commit()
