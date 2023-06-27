import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(
            "D:/mate/py-actor-manager/cinema.sqlite"
        )
        self.table_name = "actors"
        self.cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?);",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in self.cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_,)
        )
        self._connection.commit()
