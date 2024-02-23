import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:

        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self.connection.commit()

    def all(self) -> list[Actor]:
        rows = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in rows]

    def update(
            self,
            actor_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:

        self.connection.execute(
            f"UPDATE {self.table_name} SET "
            f"first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id: int) -> None:

        self.connection.execute(
            f"DELETE FROM {self.table_name}"
            f" WHERE id = ?",
            (actor_id,))

        self.connection.commit()
