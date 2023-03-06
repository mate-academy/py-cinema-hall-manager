import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self, db_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_info_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_info_cursor]

    def update(
        self, entity_id: int, updated_first_name: str, updated_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (updated_first_name, updated_last_name, entity_id),
        )

        self._connection.commit()

    def delete(self, entity_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} " "WHERE id = ?", (entity_id,)
        )
        self._connection.commit()
