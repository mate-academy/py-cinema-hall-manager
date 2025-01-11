import sqlite3
from models import Actor
from typing import Any


class ActorManager:
    def __init__(self: Any) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self: Any, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self: Any) -> list:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self: Any, id_to_update: int,
               new_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=? ",
            (new_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self: Any, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()
