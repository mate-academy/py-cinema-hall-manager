import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cinema_cursor = self._connection.execute(
            "SELECT *"
            "FROM actors"
        )
        return [Actor(*row) for row in cinema_cursor]

    def update(
            self,
            id_of_updating: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (first_name, last_name, id_of_updating)
        )
        self._connection.commit()

    def delete(self, id_for_delete: int) -> None:
        self._connection.execute(
            "DELETE FROM actors "
            "WHERE id = ? ",
            (id_for_delete,)
        )
        self._connection.commit()
