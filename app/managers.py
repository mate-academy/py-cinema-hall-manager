import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("db/Cinema.db")
        self.table_name = "actors"

    def create(
        self,
        first_name: str,
        last_name: str
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(
        self,
        autor_id: int,
        first_name: str,
        last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE actor_id = ?",
            (first_name, last_name, autor_id)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE actor_id = ?",
            (actor_id,)
        )
        self._connection.commit()

    def all(self) -> Actor:
        manager_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in manager_cursor]
