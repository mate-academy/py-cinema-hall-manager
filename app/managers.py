import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute("""
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
        """, (first_name, last_name))
        self.conn.commit()

        actor_id = self.cursor.lastrowid

        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()

        actors = [Actor(id=row[0],
                        first_name=row[1],
                        last_name=row[2])
                  for row in rows]
        return actors

    def update(self, actor_id: int, first_name: str, last_name: str) -> Actor:
        self.cursor.execute("""
            UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """, (first_name, last_name, actor_id))
        self.conn.commit()

        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def delete(self, actor_id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()
