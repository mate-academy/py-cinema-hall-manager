import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        print("actors_cursor", actors_cursor)

        return [Actor(*row) for row in actors_cursor]

    def update(self,
               id_to_update: int,
               first_name: str,
               last_name: str
               ) -> None:
        if first_name is not None:
            self._connection.execute(
                f"UPDATE {self.table_name} SET first_name = ? WHERE id = ?",
                (first_name, id_to_update,)
            )
        if last_name is not None:
            self._connection.execute(
                f"UPDATE {self.table_name} SET last_name = ? WHERE id = ?",
                (last_name, id_to_update,)
            )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
