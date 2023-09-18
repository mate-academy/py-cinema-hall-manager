import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    table_name: str = "actors"

    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema")

    def create(self, first_name: str, last_name: str) -> None:
        sql = (
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES(?, ?)"
        )
        self.connection.execute(sql, [first_name, last_name])
        self.connection.commit()

    def all(self) -> List[Actor]:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        actors = [Actor(*row) for row in cursor]

        return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        sql = (
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?"
        )
        self.connection.execute(sql, [first_name, last_name, id])
        self.connection.commit()

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(sql, [id])
        self.connection.commit()
