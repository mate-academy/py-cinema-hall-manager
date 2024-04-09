import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name}"
            "(first_name, last_name)"
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> list:
        actor_cursor = self._connect.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?,"
            "last_name = ?"
            "WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self._connect.commit()

    def delete(self, actor_id: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (actor_id,)
        )
        self._connect.commit()
