import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, database_path: str) -> None:
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        query = "INSERT INTO actors (first_name, last_name) VALUES (?, ?, ?)"
        self.cursor.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> object:
        query = "SELECT * FROM actors"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        actors = [Actor(*row) for row in rows]
        return actors

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        query = "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?"
        self.cursor.execute(query, (actor_id, first_name, last_name))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        query = "DELETE FROM actors WHERE id = ?"
        self.cursor.execute(query, (actor_id,))
        self.connection.commit()
