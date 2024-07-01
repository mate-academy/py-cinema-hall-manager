import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str = None, last_name: str = None) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(
            self,
            id_to_update: int,
            update_name: str = None,
            update_last_name: str = None
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (id_to_update, update_name, update_last_name)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id_to_delete,)
        )
