import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name)"
            "VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.connection.commit()

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            "SET "
            "first_name = ?, "
            "last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self.connection.commit()

    def all(self) -> List[Actor]:
        actors_object_data = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*actor) for actor in actors_object_data]

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()
