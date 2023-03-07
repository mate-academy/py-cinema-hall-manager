import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self.table_name}"
                                 f" (first_name, last_name)"
                                 f" VALUES (?, ?)", (first_name, last_name))

        self._connection.commit()

    def all(self) -> list:
        actor_manager_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actor_manager_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(f"UPDATE {self.table_name}"
                                 f" SET first_name = ?, last_name = ?"
                                 f" WHERE id = ?",
                                 (first_name, last_name, actor_id))

    def delete(self, actor_id: int) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name}"
                                 f" WHERE id = (?)", (actor_id,))
        self._connection.commit()
