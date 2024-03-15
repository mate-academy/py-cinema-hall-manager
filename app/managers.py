import sqlite3

from dataclasses import dataclass

from app.models import Actor


@dataclass
class ActorManager:

    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema_db.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?);",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> list[Actor]:
        cursor = self._connect.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self.table}"
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?;",
            (first_name, last_name, id_to_update)
        )
        self._connect.commit()

    def delete(self, id_delete: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table} WHERE id = ?;",
            (id_delete,)
        )
        self._connect.commit()
