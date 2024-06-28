import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema_db.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

    def all(self) -> list[Actor]:
        actors_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(id=actor_id, first_name=first_name, last_name=last_name)
            for actor_id, first_name, last_name in actors_cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, actor_id),
        )

    def delete(self, actor_id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=? ",
            (actor_id,)
        )
