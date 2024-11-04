import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        try:
            self._connection.execute(
                "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name)
            )
            self._connection.commit()
            actor_id = self._cursor.lastrowid
            return Actor(id=actor_id,
                         first_name=first_name,
                         last_name=last_name)

        except sqlite3.Error as e:
            print(f"Error creating actor: {e}")
            return None

    def all(self) -> list:
        try:
            cursor = self._connection.execute("SELECT * FROM actors")
            return [Actor(*row) for row in cursor]
        except sqlite3.Error as e:
            print(f"Error fetching actors: {e}")
            return []

    def update(self,
               actor_id: int,
               first_name: str = None,
               last_name: str = None) -> Actor:
        if not first_name and not last_name:
            print("Error: first_name or last_name must be provided.")
            return None
        fields = []
        values = []

        if first_name:
            fields.append("first_name = ?")
            values.append(first_name)

        if last_name:
            fields.append("last_name = ?")
            values.append(last_name)

        values.append(actor_id)
        try:
            self._connection.execute(
                f"UPDATE actors SET {", ".join(fields)} WHERE id = ?",
                values
            )
            self._connection.commit()
            # Повертаємо оновлений об'єкт Actor
            return Actor(id=actor_id,
                         first_name=first_name or "",
                         last_name=last_name or "")
        except sqlite3.Error as e:
            print(f"Error updating actor: {e}")
            return None

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
