import sqlite3

from models import Actor


class ActorManager:
    FILE_NAME = "cinema.db"
    TABLE_NAME = "actors"

    def __init__(self) -> None:
        self._connection = sqlite3.connect(self.FILE_NAME)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"""
                INSERT INTO {self.TABLE_NAME}
                (first_name, last_name) VALUES (?, ?)
            """,
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.TABLE_NAME}",
        )
        return [Actor(*row) for row in cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"""
                UPDATE {self.TABLE_NAME}
                SET first_name = ?, last_name = ?
                WHERE id = ?
            """,
            (first_name, last_name, id_),
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"""
                DELETE FROM {self.TABLE_NAME}
                WHERE id = ?
            """,
            (id_,),
        )
        self._connection.commit()
