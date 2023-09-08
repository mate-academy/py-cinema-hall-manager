import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema")
        self.table_name = "actor"
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            f"(id INTEGER PRIMARY KEY, "
            f"first_name VARCHAR(63), last_name VARCHAR(63))"
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(
            "SELECT * "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors]

    def update(
        self,
        update_id: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, update_id)
        )
        self._connection.commit()

    def delete(self, delete_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (delete_id,)
        )
        self._connection.commit()
