import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema_db")
        self._cursor = self._connection.cursor()
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> Actor:
        self._cursor.execute("""
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, last_name))
        self._connection.commit()
        actor_id = self._cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        self._cursor.execute("SELECT * FROM actors")
        actors = self._cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in actors]

    def update(self, actor_id: int, first_name: str, last_name: str) -> bool:
        self._cursor.execute("""
            UPDATE actors 
            SET first_name = ?, last_name = ? 
            WHERE id = ?
        """, (first_name, last_name, actor_id))
        self._connection.commit()
        return self._cursor.rowcount > 0

    def delete(self, actor_id: int) -> bool:
        self._cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self._connection.commit()
        return self._cursor.rowcount > 0
