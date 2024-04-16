import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(".../cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list:
        actors = self.connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in actors]

    def update(self, id_to_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()
