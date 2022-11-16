import sqlite3
from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> List:
        actors_coursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_coursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f" VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self,
               current_id: int,
               other_first_name: str,
               other_last_name: str) -> None:

        self._connection.execute(
            f"UPDATE {self.table_name}"
            f" SET (first_name, last_name) = (?, ?)"
            f" WHERE id = ? ",
            (other_first_name, other_last_name, current_id)
        )
        self._connection.commit()

    def delete(self, current_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (current_id,)
        )
        self._connection.commit()
