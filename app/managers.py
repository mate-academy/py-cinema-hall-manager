import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("identifier.sqlite")
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> int:
        self.cursor.execute(
            "INSERT INTO actor_manager (first_name, last_name)"
            " VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self) -> list:
        self.cursor.execute(
            "SELECT id, first_name, last_name"
            " FROM actor_manager"
        )
        return [Actor(*row) for row in self.cursor.fetchall()]

    def update(
            self, actor_id: int,
            first_name: str,
            last_name: str
    ) -> None:
        self.cursor.execute(
            "UPDATE actor_manager "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(
            "DELETE FROM actor_manager "
            "WHERE id = ?", (actor_id,))
        self.conn.commit()
