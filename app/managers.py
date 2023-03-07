import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._table_name = "actors"
        self._connection = sqlite3.connect("cinema.db3")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name}"
            f"(first_name, last_name)"
            f"VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM {self._table_name}")
        rows = cursor.fetchall()
        actors = []
        for row in rows:
            actor = Actor(*row)
            actors.append(actor)
        return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?", (first_name, last_name, id)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(f"DELETE FROM {self._table_name}"
                                 f" WHERE id=?", (id,))
        self._connection.commit()
