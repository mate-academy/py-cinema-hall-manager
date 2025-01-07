import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.db")
        self._create_table()

    def _create_table(self):
        with self.connection as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS actors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
                """
            )

    def create(self, first_name: str, last_name: str):
        with self.connection as conn:
            cursor = conn.execute(
                "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name),
            )
            return cursor.lastrowid

    def all(self):
        with self.connection as conn:
            cursor = conn.execute("SELECT id, first_name, last_name FROM actors")
            return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in cursor.fetchall()]

    def update(self, actor_id: int, first_name: str, last_name: str):
        with self.connection as conn:
            conn.execute(
                "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
                (first_name, last_name, actor_id),
            )

    def delete(self, actor_id: int):
        with self.connection as conn:
            conn.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
