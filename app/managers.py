import sqlite3
from models import Actor


class ActorFormatManagers:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self.table_name} "
                                 f"(first_name, last_name) VALUES (?, ?)",
                                 (first_name, last_name))
        self._connection.commit()

    def update(
            self,
            id_for_update: int,
            first_name_for_update: str,
            last_name_for_update: str
    ) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 f"SET first_name = ?, last_name = ? "
                                 f"WHERE id = ?",
                                 (first_name_for_update,
                                  last_name_for_update,
                                  id_for_update))

        self._connection.commit()

    def delete(self, id_for_delete: int) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name}"
                                 f" WHERE id = ?", (id_for_delete,))

        self._connection.commit()
