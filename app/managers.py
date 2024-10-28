import os.path
import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        path = os.path.join("..", "cinema.sqlite")
        self._connection = sqlite3.connect(path)
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.cursor().execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.cursor().execute(
            f"SELECT * FROM {self.table_name}"
        )
        self._connection.commit()
        return [Actor(*row) for row in actor_cursor]

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.cursor().execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.cursor().execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id_to_delete,)
        )
        self._connection.commit()
