import sqlite3
from typing import List

from models import Actor


class ActorManager:
    "Create ActorManager class"

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        "Create a new actor"
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        "Getting all records from the table"
        cursor = self._connection.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in cursor]

    def update(self, id_to_update: int, new_name: str, new_last_name: str) -> None:
        "Update record by id"
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (id_to_update, new_name, new_last_name),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        "Delete record by id"
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()
