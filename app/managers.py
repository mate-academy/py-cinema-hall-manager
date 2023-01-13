import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema")

    def all(self) -> list:
        actor_data_cursor = self._connection.execute(
            "SELECT id, first_name, last_name FROM actors"
        )
        return [Actor(*row) for row in actor_data_cursor]

    def create(
            self,
            first_name_: str,
            last_name_: str
    ) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_,)
        )
        self._connection.commit()

    def update(
            self,
            id_to_update: int,
            first_name_: str,
            last_name_: str
    ) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name_, last_name_, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
