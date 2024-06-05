import os
import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connention = sqlite3.connect(
            os.path.join("app", "cinema.sqlite")
        )
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connention.execute(
            f"INSERT INTO {self.table_name}"
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connention.commit()

    def all(self) -> list:
        actor_cursor = self._connention.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, id: int, new_first_name: int, new_last_name: str) -> None:
        self._connention.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, id),
        )

    def delete(self, id: int) -> None:
        self._connention.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id,)
        )
