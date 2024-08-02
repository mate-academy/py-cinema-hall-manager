import sqlite3
from typing import List
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        """Initialize the ActorManager, connecting to the SQLite database."""
        self.connection = sqlite3.connect("identifier.sqlite")
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        """Create a new actor entry in the database.

        Args:
            first_name (str): The first name of the actor.
            last_name (str): The last name of the actor.
        """
        query = "INSERT INTO actors (first_name, last_name) VALUES (?, ?)"
        values = (first_name, last_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def all(self) -> List[Actor]:
        """Retrieve all actor entries from the database.

        Returns:
            List[Actor]: A list of Actor instances.
        """
        actor_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        """Update an actor entry in the database.

        Args:
            actor_id (int): The ID of the actor to update.
            first_name (str): The new first name of the actor.
            last_name (str): The new last name of the actor.
        """
        query = "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?"
        values = (first_name, last_name, actor_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        """Delete an actor entry from the database.

        Args:
            actor_id (int): The ID of the actor to delete.
        """
        query = "DELETE FROM actors WHERE id = ?"
        self.cursor.execute(query, (actor_id,))
        self.connection.commit()
