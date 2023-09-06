import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

        with self._connection:
            self._connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                "id INTEGER PRIMARY KEY, "
                "first_name VARCHAR(50) NOT NULL, "
                "last_name VARCHAR(50) NOT NULL"
                ")"
            )

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} "
                 f"(first_name, last_name) VALUES (?, ?)")
        self._connection.execute(query, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT * FROM {self.table_name}"
        actors_cursor = self._connection.execute(query)

        return [Actor(*row) for row in actors_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        query = (
            f"UPDATE {self.table_name} SET first_name = ?,"
            f" last_name = ? WHERE id = ?"
        )
        self._connection.execute(query, (first_name, last_name, actor_id))
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self._connection.execute(query, (actor_id,))
        self._connection.commit()
