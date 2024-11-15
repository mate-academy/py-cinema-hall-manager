import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name: str = "cinema.sqlite") -> None:
        self.connection = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self) -> None:
        """Create the actors table if it does not already exist."""
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS actors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                )
                """
            )

    def create(self, first_name: str, last_name: str) -> Actor:
        """Insert a new actor entry into the database."""
        with self.connection:
            cursor = self.connection.execute(
                "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name),
            )
            actor_id = cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        """Retrieve all actors from the database."""
        cursor = self.connection.execute(
            "SELECT id, first_name, last_name FROM actors"
        )
        actors = [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in cursor.fetchall()
        ]
        return actors

    def update(
        self, actor_id: int, first_name: str = None, last_name: str = None
    ) -> None:
        """Update an actor's first_name and/or last_name by ID."""
        if not first_name and not last_name:
            raise ValueError(
                "At least one field (first_name or last_name) "
                "must be provided to update."
            )

        updates = []
        parameters = []

        if first_name:
            updates.append("first_name = ?")
            parameters.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            parameters.append(last_name)

        parameters.append(actor_id)

        with self.connection:
            self.connection.execute(
                f"UPDATE actors SET {", ".join(updates)} WHERE id = ?",
                parameters,
            )

    def delete(self, actor_id: int) -> None:
        """Delete an actor from the database by ID."""
        with self.connection:
            self.connection.execute(
                "DELETE FROM actors WHERE id = ?", (actor_id,)
            )
