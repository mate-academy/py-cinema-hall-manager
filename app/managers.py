import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema")
        self.default_table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.default_table} "
            "(first_name, last_name) "
            "VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.default_table}"
        )
        return [Actor(*row) for row in cursor]

    def update(
            self,
            first_name: str,
            last_name: str,
            id_to_update: int
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.default_table} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.default_table} "
            "WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()
