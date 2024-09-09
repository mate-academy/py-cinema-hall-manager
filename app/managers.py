import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_format_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )

        return [
            Actor(*row) for row in actor_format_cursor
        ]

    def create(self, first_name: str,
               last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str,
               new_last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET (first_name, last_name) = (?, ?)"
            "WHERE ID = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE ID = ?;",
            (id_to_delete,)
        )
        self._connection.commit()
