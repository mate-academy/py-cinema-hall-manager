import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_path: str = "cinema.db") -> None:
        # Create database and table if not exists
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """)
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute("""
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute("""
            UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """, (first_name, last_name, actor_id))
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()
