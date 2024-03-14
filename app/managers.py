import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(self, row_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (first_name, last_name, row_id)
        )
        self.connection.commit()

    def delete(self, row_id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (row_id,)
        )
        self.connection.commit()
