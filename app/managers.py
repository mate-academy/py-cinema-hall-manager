import sqlite3
from models import Actor
from typing import List


class ActorManager:
    def __init__(self, database_name: str = "cinema.db") -> None:
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create(self, actor: Actor) -> None:
        self.cursor.execute("INSERT INTO actors (first_name, last_name) "
                            "VALUES (?, ?)",
                            (actor.first_name, actor.last_name))
        self.conn.commit()

    def all(self) -> List[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        actors = [Actor(*row) for row in rows]
        return actors

    def update(self, first_name: str, last_name: str, actor_id: int) -> None:
        self.cursor.execute("UPDATE actors SET first_name = ?,"
                            " last_name = ? WHERE id = ?",
                            (first_name, last_name, actor_id))
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?",
                            (actor_id,))
        self.conn.commit()
