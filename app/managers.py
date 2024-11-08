import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name: str = "cinema.db") -> None:
        self.db_name = db_name

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_name)
        return conn

    def create(self, first_name: str, last_name: str) -> None:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        conn.commit()
        conn.close()

    def all(self) -> list:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM actors")
        rows = cursor.fetchall()
        actors = [
            Actor(id=row[0], first_name=row[1],
                  last_name=row[2]) for row in rows
        ]
        conn.close()
        return actors

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE actors SET first_name = ?,"
                       " last_name = ? WHERE id = ?",
                       (first_name, last_name, actor_id))
        conn.commit()
        conn.close()

    def delete(self, actor_id: int) -> None:

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        conn.commit()
        conn.close()
