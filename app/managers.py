import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")
        self.connection.row_factory = sqlite3.Row

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        return [
            Actor(**i)
            for i in self.connection.execute("SELECT * FROM actors").fetchall()
        ]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_)
        )
        self.connection.commit()

    def delete(self, id_: int) -> None:
        self.connection.execute(
            "DELETE FROM actors "
            "WHERE id = ?",
            (id_,)
        )
        self.connection.commit()
