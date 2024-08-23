import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            """
            INSERT INTO ?
            (first_name, last_name) VALUES (?, ?)
            """,
            (self.table_name, first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            actor_id: int,
            first_name_to_update: str,
            last_name_to_update: str
    ) -> None:

        self._connection.execute(
            """
            UPDATE ?
            SET (first_name, last_name) = (?, ?)
            WHERE id = ?
            """,
            (
                self.table_name,
                first_name_to_update,
                last_name_to_update, actor_id
            )
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
