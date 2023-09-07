import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection: sqlite3.Connection = sqlite3.connect("cinema.db")
        self.table_name: str = "actors"

        with self._connection:
            self._connection.execute(
                f"CREATE TABLE {self.table_name}"
                "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "first_name VARCHAR(15) NOT NULL,"
                "last_name VARCHAR(15) NOT NULL);"
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name)"
                "VALUES (?, ?);",
                (first_name, last_name),
            )

    def all(self) -> list[Actor]:
        actor_cursor: sqlite3.Cursor = self._connection.execute(
            "SELECT * "
            f"FROM {self.table_name};"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                "SET first_name = ?, last_name = ? "
                "WHERE id = ?;",
                (first_name, last_name, id),
            )

    def delete(self, id: int) -> None:
        with self._connection:
            self._connection.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?;", (id,)
            )
