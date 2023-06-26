import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connetcion = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connetcion.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connetcion.commit()

    def all(self) -> list[Actor]:
        actors_data = self._connetcion.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_data]

    def update(self, id_to_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self._connetcion.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connetcion.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connetcion.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connetcion.commit()
