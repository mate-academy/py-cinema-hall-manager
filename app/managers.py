import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            " VALUES (?, ?)", (first_name, last_name,))
        self._connection.commit()

    def update(self, new_first_name: str,
               new_last_name: str,
               new_id: int):
        self._connection.execute(
            f"UPDATE {self.table_name} SET"
            f" first_name = ? AND last_name = ? WHERE id = ? ",
            (new_first_name, new_last_name, new_id,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
