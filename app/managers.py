import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema_db.sqlite")
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self.conn.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self.conn.execute(
            "SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name:
            str
    ) -> None:
        self.conn.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self.conn.commit()

    def delete(self, id_to_delete: int) -> None:
        self.conn.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self.conn.commit()
