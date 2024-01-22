import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, actor_id)
        )

        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (actor_id,)
        )

        self.conn.commit()
