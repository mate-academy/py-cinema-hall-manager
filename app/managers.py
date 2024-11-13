import sqlite3
from models import Actor


class ActorManager:

    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

    def all(self):
        cinema_actor_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [Actor(*obj) for obj in cinema_actor_cursor.fetchall()]

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def update(self, obj_id: int, first_name: str, last_name: str, ):
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, obj_id)
        )
        self._connection.commit()

    def delete(self, obj_id):
        self._connection.execute(
            f"DELETE FROM {self._table_name}  WHERE id = ?", (obj_id,)
        )
        self._connection.commit()
