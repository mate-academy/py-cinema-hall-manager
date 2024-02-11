import sqlite3
import os
from models import Actor

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(os.path.join(
            parent_directory, "cinema.sqlite"))
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*actor) for actor in actors_cursor
        ]

    def update(self, id: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id)
        )

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id,)
        )
