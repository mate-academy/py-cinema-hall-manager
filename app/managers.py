import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table = "actors"
        self._connection.execute("""
                                CREATE TABLE IF NOT EXISTS actors (
                                id INTEGER PRIMARY KEY,
                                first_name VARCHAR NOT NULL,
                                last_name VARCHAR NOT NULL
                                );
                                """)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            "SET id = ?, first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (actor_id, first_name, last_name)
        )
        self._connection.commit()

    def delete(self, actor_id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} WHERE id = ?",
            (actor_id_to_delete,)
        )
        self._connection.commit()
