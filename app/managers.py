import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table = "actors"

    def create(self, first_name_to_add: str, last_name_to_add: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES(?, ?)",
            (first_name_to_add, last_name_to_add)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_cursor = self._connection.execute(f"SELECT * FROM {self.table}")
        return [
            Actor(*row)
            for row in actors_cursor
        ]

    def update(
            self,
            id_to_update: int,
            first_name_to_update: str,
            last_name_to_update: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table} SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (first_name_to_update, last_name_to_update, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
