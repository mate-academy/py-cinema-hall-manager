import sqlite3

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._db = sqlite3.connect("../cinema.sqlite")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._db.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) "
            "VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._db.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._db.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [
            Actor(
                id=id,
                first_name=first_name,
                last_name=last_name
            ) for first_name, last_name, id in actors_cursor
        ]

    def update(
            self,
            id: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._db.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id)
        )
        self._db.commit()

    def delete(self, id: int) -> None:
        self._db.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ? ",
            (id,)
        )
        self._db.commit()
