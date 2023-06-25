import sqlite3

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    # CREATE
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    # RETRIEVE (READ)
    def all(self) -> list:
        actor_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    # UPDATE
    def update(
            self, id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?"
            "WHERE id = ?",
            (new_first_name, id_to_update)
        )
        self._connection.commit()
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET last_name = ?"
            "WHERE id = ?",
            (new_last_name, id_to_update)
        )
        self._connection.commit()

    # DELETE
    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
