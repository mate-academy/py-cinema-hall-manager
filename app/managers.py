import os
import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(os.path.join("..", "cinema"))
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        literary_formats_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in literary_formats_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?,  last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id)
        )

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id, )
        )
