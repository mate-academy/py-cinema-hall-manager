import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.db")
        self.cur = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cur.execute(
            """
        INSERT INTO actors(first_name, last_name)
        VALUES(?, ?)
        """,
            (first_name, last_name),
        )
        self.conn.commit()

        actor_id = self.cur.lastrowid

        return Actor(actor_id, first_name, last_name)

    def all(self) -> list[Actor]:
        actors = self.cur.execute("SELECT * FROM actors").fetchall()

        return [Actor(*actor) for actor in actors]

    def update(self, actor_id: int, first_name: str, last_name: str) -> Actor:
        self.cur.execute(
            """
            UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """,
            (first_name, last_name, actor_id),
        )
        self.conn.commit()

        return Actor(actor_id, first_name, last_name)

    def delete(self, actor_id: int) -> Actor:
        self.cur.execute(
            """
        DELETE FROM actors
        WHERE id = ?
        """,
            (actor_id,),
        )
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()
