import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"
        self.create_table()

    def create_table(self) -> None:
        with self._connection:
            self._connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
                """
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"""
                INSERT INTO {self.table_name} (first_name, last_name)
                VALUES (?, ?)
                """,
                (first_name, last_name)
            )

    def all(self) -> list[Actor]:
        with self._connection:
            read_actors = self._connection.execute(
                f"""
                SELECT *
                FROM {self.table_name}
                """
            )
        return [Actor(*row) for row in read_actors.fetchall()]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"""
                UPDATE {self.table_name}
                SET first_name = ?, last_name = ?
                WHERE id = ?
                """,
                (first_name, last_name, id)
            )

    def delete(self, id: int) -> None:
        with self._connection:
            self._connection.execute(
                f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
                """,
                (id,)
            )
