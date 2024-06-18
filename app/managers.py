import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> list[Actor]:
        actor_format_cursor = self._connect.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [
            Actor(*row) for row in actor_format_cursor
        ]

    def update(
            self, id_to_update: int, new_first_name: str, new_last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connect.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connect.commit()
