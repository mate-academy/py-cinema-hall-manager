import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        actor_manager_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name};"
        )
        return [Actor(*row) for row in actor_manager_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update: int,
               first_name_upd: str,
               last_name_upd: str) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 "SET first_name = ?, last_name = ? "
                                 "WHERE id = ?",
                                 (first_name_upd, last_name_upd, id_to_update))
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = (?)", (id_to_delete,)
        )
        self._connection.commit()
