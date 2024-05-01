from models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("di.db")
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.commit()

    def all(self) -> list:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self,
               actor_id: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.cursor.execute("""
            UPDATE actors SET first_name=?, last_name=? WHERE id=?
        """, (new_first_name, new_last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id=?", (actor_id,))
        self.connection.commit()
