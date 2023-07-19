import sqlite3

from models import Actor

from typing import List


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("D:/sqlitestudio/cinema.db3")

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_,)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors_data = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in actors_data]

    def update(
            self,
            id_: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name =? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            "DELETE FROM actors "
            "WHERE id = ?",
            (id_,)
        )
        self._connection.commit()
