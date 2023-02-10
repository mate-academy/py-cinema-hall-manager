import sqlite3
from typing import List

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,))

        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            row_id: int,
            first_name: str,
            last_name: str,
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?,"
            f"last_name = ?"
            f"WHERE id = ?",
            (first_name, last_name, row_id)
        )
        self._connection.commit()

    def delete(
            self,
            row_id: int
    ) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (row_id,)
        )
        self._connection.commit()
