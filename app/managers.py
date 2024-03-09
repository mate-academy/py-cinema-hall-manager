import sqlite3
from models import Actor
from typing import List


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.sqlite")
        self.table_name: str = "Actor"

    def create(self, format_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actor_cursor = self._connection.execute(
            "SELECT * FROM Actor"
        )
        return [
            Actor(*actor) for actor in actor_cursor
        ]

    def update(self, actor_to_id: int, new_format_: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET format = ? "
            "WHERE actor_id = ?",
            (new_format_, actor_to_id)
        )
        self._connection.commit()

    def delete(self, actor_to_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE actor_id = ?",
            (actor_to_id,)
        )
        self._connection.commit()
