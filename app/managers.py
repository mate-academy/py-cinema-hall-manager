import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._actors_manager = sqlite3.connect("../cinema.sqlite")

    def all(self) -> list[Actor]:
        cursor = self._actors_manager.execute(
            "SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._actors_manager.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._actors_manager.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._actors_manager.execute(
            "UPDATE actors SET "
            "first_name = ?,"
            "last_name = ?"
            "WHERE id = ?",
            (first_name, last_name, id)
        )
        self._actors_manager.commit()

    def delete(self, id: int) -> None:
        self._actors_manager.execute(
            "DELETE FROM actors WHERE id = ?",
            (id,)
        )
        self._actors_manager.commit()
