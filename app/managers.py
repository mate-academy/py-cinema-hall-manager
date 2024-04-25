from models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("database/cinema.db")
        self.table_name = "actors"
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            "(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)"
        )

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_actor: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            [first_name, last_name, id_actor]
        )
        self._connection.commit()

    def delete(self, id_del: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_del,)
        )
        self._connection.commit()
