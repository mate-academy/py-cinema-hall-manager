import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._conn = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors1"

    def create(self, first_name: str, last_name: str):
        self._conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._conn.commit()

    def update(self, id_actor: int, new_first_name: str, new_last_name: str):
        self._conn.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id_actor = ? ",
            (new_first_name, new_last_name, id_actor,)
        )
        self._conn.commit()

    def delete(self, id_to_delete: int):
        self._conn.execute(
            f"DELETE FROM {self.table_name} WHERE id_actor = ? ",
            (id_to_delete,)
        )
        self._conn.commit()

    def all(self):
        cinema_cursor = self._conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cinema_cursor
        ]
