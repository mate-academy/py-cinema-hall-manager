import sqlite3
from typing import List

from app.models import Actor


class ActorManager:

    def __init__(self) -> None:
        self.connection = sqlite3.connect("/Users/khrypunov/"
                                          "PycharmProjects/"
                                          "py-actor-manager/cinema.sqlite")
        self.name_db = "actors"

    def all(self) -> List[Actor]:
        inform = self.connection.execute(f"SELECT * FROM {self.name_db}")
        return [Actor(*row) for row in inform.fetchall()]

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.name_db} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def update(self, id_actor: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.name_db}"
            f" SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_actor)
        )
        self.connection.commit()

    def delete(self, id_actor: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.name_db} WHERE id = ?",
            (id_actor,)
        )
        self.connection.commit()
