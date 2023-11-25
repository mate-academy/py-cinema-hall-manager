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
            f"INSERT INTO actors (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name)
        )

    def all(self) -> List[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM actors"
        )

        return [Actor(*info) for info in actor_cursor]

    def update(
            self,
            id_number: id,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE actors "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_number)
        )

    def delete(self, id_number: int) -> None:
        self._connection.execute(
            f"DELETE FROM actors "
            f"WHERE id = (?)",
            (id_number,)
        )
