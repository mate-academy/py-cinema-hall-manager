import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.name_tabl = "actors"
        self._connection = sqlite3.connect("cinema.db3")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.name_tabl} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.name_tabl}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.name_tabl} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.name_tabl} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
