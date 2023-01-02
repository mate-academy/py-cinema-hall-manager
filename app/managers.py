import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.db")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cinema_actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table}"
        )
        return [Actor(*row) for row in cinema_actors_cursor]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
            f"WHERE id = ?",
            (id, )
        )
        self._connection.commit()
