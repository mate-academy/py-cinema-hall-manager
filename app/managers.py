import sqlite3

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.data_base = "cinemas"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.data_base} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        data = self._connection.execute(
            f"SELECT * FROM {self.data_base}"
        )
        return [Actor(*actor) for actor in data]

    def update(self, pk: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.data_base} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (first_name, last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.data_base} "
            f"WHERE id = ?",
            (pk,)
        )
        self._connection.commit()
