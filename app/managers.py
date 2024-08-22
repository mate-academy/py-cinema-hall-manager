import sqlite3

from models import Actor


class ActorManager:
    def __init__(self, db_path: str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actor (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL
            )
        """)
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty")

        self.cursor.execute("""
            INSERT INTO actor (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, first_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute("""
            SELECT id, first_name, last_name
            FROM actor
        """)
        rows = self.cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty")

        self.cursor.execute("""
            UPDATE actor
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """, (first_name, last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("""
            DELETE FROM actor
            WHERE id = ?
        """, (actor_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
