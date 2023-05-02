import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite3")
        self.table_name = "actors"
        self._connection.execute("CREATE TABLE "
                                 f"IF NOT EXISTS {self.table_name}("
                                 "id INTEGER PRIMARY KEY, "
                                 "first_name VARCHAR(255), "
                                 "last_name VARCHAR(255)"
                                 ")")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> List:
        actors_data = self._connection.execute("SELECT * FROM actors")
        return [Actor(*row) for row in actors_data]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
