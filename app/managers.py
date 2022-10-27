import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self):
        self._db = sqlite3.connect("d:/ma/cinema.db")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._db.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name))
        self._db.commit()

    def all(self):
        actors_cursor = self._db.execute(
            f"SELECT id, first_name, last_name FROM {self._table_name}")

        return [Actor(*row) for row in actors_cursor]

    def update(self, row_id: int, first_name: str, last_name: str):
        self._db.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, row_id))
        self._db.commit()

    def delete(self, row_id: int):
        self._db.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (row_id,))
        self._db.commit()
