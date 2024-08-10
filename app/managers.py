import sqlite3
import os

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "cinema.sqlite")
        self._connection = sqlite3.connect(db_path)
        self.table_name = "actors"

    def create(self, first_name, last_name) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, id_to_update: int, first_name, last_name) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
