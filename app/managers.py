import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema")

    def all(self) -> list:
        data = self._connection.execute("SELECT id, first_name, "
                                        f"last_name FROM {self.table_name}")
        return [Actor(*row) for row in data]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self.table_name} "
                                 "(first_name, last_name) VALUES (?, ?)",
                                 (first_name, last_name,))
        self._connection.commit()

    def update(self, new_id: int, new_first: str, new_last: str) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 "SET first_name = ?"
                                 "AND last_name = ?"
                                 "WHERE id = ?",
                                 (new_first, new_last, new_id, ))
        self._connection.commit()

    def delete(self, id_to_del: int) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name} "
                                 "WHERE id = ?",
                                 (id_to_del,))
        self._connection.commit()
