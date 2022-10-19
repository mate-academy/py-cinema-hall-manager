import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) "
            f"VALUES (?, ?);",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        data_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name from {self.table};"
        )
        return [Actor(*row) for row in data_cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            f"where id = ?;",
            (first_name, last_name, id_)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} WHERE id = ?",
            (id_,)
        )
        self._connection.commit()
