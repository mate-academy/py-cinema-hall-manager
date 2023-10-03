import sqlite3
from models import Actor
from typing import List


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect(
            "C:/Users/user/Desktop/djiango-orm/cinema"
        )
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> List[Actor]:
        cinema_cursor = self._connect.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in cinema_cursor
        ]

    def update(
            self,
            updated_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, updated_id)
        )
        self._connect.commit()

    def delete(self, id_to_del: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_del,)
        )
        self._connect.commit()
