import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.db3")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )

        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            "SELECT *"
            f"FROM {self._table_name}"
        )

        return [Actor(*row) for row in actor_cursor]

    def update(
            self, needed_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, needed_id)
        )

        self._connection.commit()

    def delete(self, needed_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (needed_id,)
        )

        self._connection.commit()
