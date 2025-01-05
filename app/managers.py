import sqlite3
from models import Actor

class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str):
        self.connection.execute(
            "INSERT INTO actors(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()


    def all(self):
        actors_cursor = self.connection.execute(
            f"SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]


    def update(self, id: int, first_name: str, last_name: str):
        self.connection.execute(
            f"UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id,)
        )
        self.connection.commit()

    def delete(self, id: int):
        self.connection.execute(
            f"DELETE FROM actors WHERE id = ?",
            (id,)
        )
