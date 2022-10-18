import sqlite3

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect(
            "D:\\mate_academy\\django-orm\\py-actor-manager\\cinema.sqlite"
        )
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name}"
            "(first_name, last_name)"
            "VALUES(?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_data_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )

        return [Actor(*actor_data) for actor_data in actor_data_cursor]

    def update(self, _id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?,"
            "last_name = ? "
            "WHERE id = ? ",
            (first_name, last_name, _id)
        )
        self._connection.commit()

    def delete(self, _id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?",
            (_id,)
        )
        self._connection.commit()
