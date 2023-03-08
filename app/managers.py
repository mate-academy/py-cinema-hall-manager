import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self.table}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            name: str,
            surname: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (name, surname, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
