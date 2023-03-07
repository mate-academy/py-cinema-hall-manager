import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self, db_file: str = "cinema.db3") -> None:
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute("INSERT INTO actors (first_name, last_name)"
                            " VALUES (?, ?)",
                            (first_name, last_name))
        self.connect.commit()

    def all(self) -> List[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        actors = []
        for row in self.cursor.fetchall():
            actor = Actor(*row)
            actors.append(actor)
        return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute("UPDATE actors SET first_name = ?,"
                            " last_name = ? WHERE id = ?",
                            (first_name, last_name, id))
        self.connect.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.connect.commit()
