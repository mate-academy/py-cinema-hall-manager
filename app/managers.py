import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name: str = "cinema.sqlite") -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute("""
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        actors = [
            Actor(
                id=row[0],
                first_name=row[1],
                last_name=row[2]
            ) for row in rows]
        return actors

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        if first_name:
            self.cursor.execute("""
                UPDATE actors
                SET first_name = ?
                WHERE id = ?
            """, (first_name, actor_id))
        if last_name:
            self.cursor.execute("""
                UPDATE actors
                SET last_name = ?
                WHERE id = ?
            """, (last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.connection.commit()
