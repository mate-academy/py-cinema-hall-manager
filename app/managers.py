import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

    def all(self) -> list[Actor]:
        all_lines = self._connection.execute(
            f"""
                SELECT *
                FROM {self.table_name}
            """
        )
        return [Actor(*line) for line in all_lines]

    def create(self, **kwvalues) -> None:
        self._connection.execute(
            f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
            """,
            tuple(kwvalues.values())
        )
        self._connection.commit()

    def update(self, id: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"""
                UPDATE {self.table_name}
                SET first_name = ?,
                    last_name = ?
                WHERE id = ?
            """,
            (new_first_name, new_last_name, id)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
            """,
            (id,)
        )
        self._connection.commit()
