import sqlite3
from dataclasses import dataclass
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
                                 (first_name, last_name,))
        self._connection.commit()

    def all(self):
        cinema_data_cursor = self._connection.execute("SELECT id, first_name, last_name FROM actors")
        return [Actor(*row) for row in cinema_data_cursor]

    def update(self, id_to_update: int, new_actor_first_name: str, new_actor_last_name: str):
        self._connection.execute(f"UPDATE {self.table_name} "
                                 "SET first_name = ?, last_name = ? "
                                 "WHERE id = ? ",
                                 (new_actor_first_name, new_actor_last_name,
                                  id_to_update)
                                 )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(f"DELETE FROM {self.table_name} "
                                 f"WHERE id = ?",
                                 (id_to_delete,))
        # self._connection.execute(f"DELETE FROM {self.table_name}")
        self._connection.commit()
