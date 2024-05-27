import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self._cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self._cursor.execute("""
        INSERT INTO actors (first_name, last_name)
        VALUES (?, ?)""", (first_name, last_name))

        self._connection.commit()

    def all(self) -> list[Actor]:
        self._cursor.execute("SELECT * FROM actors")
        return [Actor(*row) for row in self._cursor.fetchall()]

    def update(self,
               id_to_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self._cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._cursor.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,))
        self._connection.commit()
