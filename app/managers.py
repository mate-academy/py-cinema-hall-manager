import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("app/cinemadb.sqlite3")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) "
            "VALUES (?,?);",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name};")
        return [Actor(*row) for row in actors_cursor]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(f"UPDATE {self._table_name} "
                                 "SET first_name= ?, last_name= ?"
                                 " WHERE id = ?;",
                                 (first_name, last_name, id))

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?", (id,))
        self._connection.commit()
