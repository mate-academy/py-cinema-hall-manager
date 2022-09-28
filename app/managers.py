import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(self, id_, new_first_name, new_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_)
        )
        self._connection.commit()

    def delete(self, delete_id):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (delete_id,)
        )
        self._connection.commit()
