import sqlite3
from dataclasses import dataclass

from models import Actor


@dataclass
class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name, last_name) -> None:
        self._connection.execute(
            f"insert into {self.table_name} (first_name, last_name) values (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"select * from {self.table_name}"
        )
        self._connection.commit()
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update, first_name, last_name) -> None:
        self._connection.execute(
            f"update {self.table_name} "
            "set first_name = ?, last_name = ? "
            "where id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete) -> None:
        self._connection.execute(
            f"delete from {self.table_name} where id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
