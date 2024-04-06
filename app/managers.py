import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self.connection.commit()

    def all(self) -> list[Actor]:
        cinema_cursor = self.connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [Actor(*row) for row in cinema_cursor]

    def update(
            self,
            actor_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (new_first_name, new_last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table} WHERE id = ?", (actor_id,)
        )
        self.connection.commit()
