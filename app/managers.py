import sqlite3
from models import Actor
import os


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            os.path.dirname(os.getcwd()) + "/cinema.sqlite"
        )
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list:
        cursor = (self.connection.execute(
            f"SELECT * FROM {self.table}"
        ))
        return [Actor(*row) for row in cursor]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id)
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table} WHERE id = ?",
            (id,)
        )
        self.connection.commit()
