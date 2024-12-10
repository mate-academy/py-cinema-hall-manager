import sqlite3
from models import Actor


class ActorManager:

    def __init__(self):
        self._connection = sqlite3.connect('cinema.sqlite')
        self.table_name = 'actors'

    def create(self, first_name: str, last_name: str) -> None:

        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):

        format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in format_cursor]

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):

        self._connection.execute(
        f"UPDATE {self.table_name} "
            "SET format = ? "
            "WHERE id = ?",
            (new_last_name, new_first_name, id_to_update,)
        )

        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()

