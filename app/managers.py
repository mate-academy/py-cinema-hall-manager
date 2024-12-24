import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute("INSERT INTO actors (first_name, last_name)"
                          "VALUES (?, ?)",
                          (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM actors")
        return [Actor(*row) for row in cursor.fetchall()]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE actors SET first_name = ?, last_name = ?"
                       "WHERE id = ?",
                       (first_name, last_name, id))
        self.conn.commit()

    def delete(self, id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM actors"
                       "WHERE id = ?",
                       (id))
        self.conn.commit()
