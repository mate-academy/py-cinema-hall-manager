import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id=?", (actor_id,)
        )
        self._connection.commit()
