import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.db")
        self.table_name = "actors"

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name_, last_name_,)
        )
        self._connection.commit()

    def all(self) -> list:
        cinema_actors_cursor = self._connection.execute(
            "SELECT *"
            f"FROM {self.table_name}"
        )

        return [Actor(*row) for row in cinema_actors_cursor]

    def update(self, id_to_update: int, new_fn: str, new_ln: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_fn, new_ln, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
