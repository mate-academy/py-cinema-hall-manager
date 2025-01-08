import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name } (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def update(self, actor_id, first_name, last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id),
        )
        self._connection.commit()

    def all(self):
        actor_manager_cursor = self._connection.execute(
            f"SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in actor_manager_cursor
        ]

    def delete(self, actor_id):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (actor_id,),
        )
        self._connection.commit()
