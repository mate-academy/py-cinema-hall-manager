import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema")
        self.table_names = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_names} ("
            f"first_name, last_name"
            f") VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_data_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_names}"
        )

        return [Actor(*row) for row in actors_data_cursor]

    def update(
            self, id_to_update: int,
            new_name: str,
            new_lastname: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_names} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_name, new_lastname, id_to_update),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_names} " "WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()
