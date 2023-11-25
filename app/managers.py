import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name)"
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actor_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )

        return [Actor(*info) for info in actor_cursor]

    def update(
            self,
            id_number: id,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_number)
        )
        self._connection.commit()

    def delete(self, id_number: int) -> None:
        self._connection.execute(
            "DELETE FROM actors "
            "WHERE id = (?)",
            (id_number,)
        )
        self._connection.commit()
