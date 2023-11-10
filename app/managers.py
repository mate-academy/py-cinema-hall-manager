import sqlite3

from models import Actors


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self._table_name}"
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self._connect.commit()

    def all(self) -> list:
        actors_date = self._connect.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [Actors(*row) for row in actors_date]

    def update(
            self,
            id_: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (first_name, last_name, id_)
        )
        self._connect.commit()

    def delete(self, id_: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (id_,)
        )
        self._connect.commit()
