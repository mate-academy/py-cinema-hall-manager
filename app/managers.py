import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._conection = sqlite3.connect("cinema.db3")
        self.table_name = "Actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._conection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        self._conection.commit()

    def all(self) -> list:
        actors_cursor = self._conection.execute(
            f"SELECT id, first_name, last_name " f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
        self, id_to_update: int, new_first_name: str, new_last_name: str
    ) -> None:
        self._conection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update),
        )
        self._conection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._conection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_delete,)
        )
        self._conection.commit()
