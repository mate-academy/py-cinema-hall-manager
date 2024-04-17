import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            """
            INSERT INTO actors
            (first_name, last_name) VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self.connection.commit()

    def update(self,
               id_to_update: int,
               first_name_update: str,
               last_name_update: str) -> None:
        self.connection.execute(
            """
            UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (id_to_update, first_name_update, last_name_update)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            """
            DELETE FROM actors
            WHERE id = ?
            """,
            (id_to_delete,)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(
            """
            SELECT * FROM actors
            """
        )
        return [Actor(*row) for row in cursor]
