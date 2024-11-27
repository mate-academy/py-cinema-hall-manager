import sqlite3
from models import Actor

class ActorManager:
    def __init__(self):
        self.conn = sqlite3.connect("cinema.db")
        self._create_table()

    def _create_table(self):
        """Create the 'actors' table if it does not exist."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS actors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
            """)

    def create(self, first_name: str, last_name: str) -> None:
        """Add a new actor to the database."""
        with self.conn:
            self.conn.execute(
                "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name)
            )

    def all(self) -> list[Actor]:
        """Retrieve all actors as a list of Actor instances."""
        cursor = self.conn.execute("SELECT id, first_name, last_name FROM actors")
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in cursor.fetchall()]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        """Update an actor's details by ID."""
        with self.conn:
            self.conn.execute(
                "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
                (first_name, last_name, actor_id)
            )

    def delete(self, actor_id: int) -> None:
        """Delete an actor by ID."""
        with self.conn:
            self.conn.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
