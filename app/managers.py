import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite3")
        self._table_name = "actors"
        # self._connection.set_trace_callback(print)

        self._init_database()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name)"
            f"VALUES (:first_name, :last_name);",
            {"first_name": first_name, "last_name": last_name}
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cur = self._connection.execute(
            "SELECT id, first_name, last_name "
            f"FROM {self._table_name};"
        )
        return [Actor(*row) for row in cur]

    def update(self, entry_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = :first_name, last_name = :last_name "
            "WHERE id = :id;",
            {"id": entry_id, "first_name": first_name, "last_name": last_name}
        )
        self._connection.commit()

    def delete(self, entry_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = :id;",
            {"id": entry_id}
        )
        self._connection.commit()

    def _init_database(self) -> None:
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self._table_name} ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255)"
            ");"
        )
