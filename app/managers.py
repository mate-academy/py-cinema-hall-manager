import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            """
            INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            """
               SELECT *
               FROM actors
            """
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(
            self,
            id_to_update: int,
            firstname: str,
            lastname: str
    ) -> None:
        self._connection.execute(
            """
            UPDATE actors
            SET (first_name, last_name) = (?, ?)
            WHERE id = ?
            """,
            (firstname, lastname, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            """
            DELETE
            FROM actors
            WHERE id = ?
            """,
            (id_to_delete,)
        )
        self._connection.commit()
