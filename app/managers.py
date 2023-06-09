import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")

    def all(self) -> list:
        cinema_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in cinema_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        query = """
                INSERT INTO actors (first_name, last_name)
                VALUES (?, ?)
                """
        self._connection.execute(query, (first_name, last_name))
        self._connection.commit()

    def update(self, id_to_update: int,
               first_name: str,
               last_name: str) -> None:
        query = """
               UPDATE actors
               SET first_name = ?, last_name = ?
               WHERE id = ?
               """
        self._connection.execute(query, (first_name, last_name, id_to_update))
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        query = "DELETE FROM actors WHERE id = ?"
        self._connection.execute(query, (id_to_delete,))
        self._connection.commit()
