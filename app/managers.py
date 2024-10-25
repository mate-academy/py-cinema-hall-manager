import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.tables_actors = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.tables_actors} (first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.tables_actors}"
        )
        return [
            Actor(*actor) for actor in cursor
        ]


    def update(self, id_to_update: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.tables_actors} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete) -> None:
        self._connection.execute(
            f"DELETE FROM {self.tables_actors} "
            "WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()
