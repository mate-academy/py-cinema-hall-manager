import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connections = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connections.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connections.commit()

    def retrieve(self) -> list:
        actors_cursor = self._connections.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(self,
               id: int,
               first_name: str,
               last_name: str) -> None:
        self._connections.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (id, first_name, last_name)
        )
        self._connections.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connections.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connections.commit()
