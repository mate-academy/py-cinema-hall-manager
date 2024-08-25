import sqlite3
from models import Actor


class CinemaManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "Actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cinema_cursor = self._connection.execute(
            f"""
            SELECT * FROM {self.table_name}
            """
        )
        actors = [Actor(*row) for row in cinema_cursor]
        cinema_cursor.close()
        return actors

    def update(self, _id: int, new_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (new_name, new_last_name, _id)
        )
        self._connection.commit()

    def delete(self, _id: int) -> None:
        self._connection.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (_id,)
        )
        self._connection.commit()

    def disconnect(self) -> None:
        self._connection.close()
