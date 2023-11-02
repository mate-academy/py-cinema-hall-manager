import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema_db.db3")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            "SELECT * "
            "FROM actors"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_up: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (first_name, last_name, id_up)
        )
        self._connection.commit()

    def delete(self, id_del: int) -> None:
        self._connection.execute(
            "DELETE "
            "FROM {self.table} "
            "WHERE id = ?",
            (id_del,)
        )
        self._connection.commit()
