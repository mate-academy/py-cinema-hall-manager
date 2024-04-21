import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.name = "actors"

    def all(self) -> None:
        format_cursor = self._connection.execute(
            f"SELECT * FROM {self.name}"
        )
        return [
            Actor(*row) for row in format_cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def update(self, new_name: str, new_last_name: str, id: int) -> None:
        self._connection.execute(
            f"UPDATE {self.name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_name, new_last_name, id),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
