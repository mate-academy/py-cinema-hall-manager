import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema_db.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_manager_cursor = self._connection.execute("SELECT * FROM actors")
        return [Actor(*row) for row in actor_manager_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE actor_id = ?",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()
