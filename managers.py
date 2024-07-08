import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self.connection.execute(f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
                                (first_name, last_name))
        self.connection.commit()

    def all(self):
        actor_cursor = self.connection.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row in actor_cursor]

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self.connection.execute(f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
                                (new_first_name, new_last_name, id_to_update))
        self.connection.commit()

    def delete(self, id_to_delete: int):
        self.connection.execute(f"DELETE FROM {self.table_name} WHERE id = ?",
                                (id_to_delete,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
