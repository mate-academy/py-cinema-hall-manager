import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection_ = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> List[Actor]:
        cursor = self.connection_.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self.connection_.execute(
            f"INSERT INTO {self.table_name}"
            " (first_name , last_name) VALUES(?,?)",
            (first_name, last_name)
        )
        self.connection_.commit()

    def delete(self, delete_id: int) -> None:
        self.connection_.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (delete_id,)
        )
        self.connection_.commit()

    def update(
            self, new_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.connection_.execute(
            f"UPDATE {self.table_name}"
            " SET first_name = ?,last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, new_id,)
        )
        self.connection_.commit()
