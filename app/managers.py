import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def all(self):
        actors_data = self._connection.execute(f"select * from {self.table_name}")
        return [Actor(*actor) for actor in actors_data]

    def create(self, first_name: str, last_name: str):
        self._connection.execute(f"insert into {self.table_name} (first_name, last_name) values (?, ?)", (first_name, last_name))
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"update {self.table_name} "
            "set first_name = ?, last_name = ? "
            "where Id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"delete from {self.table_name} "
            f"where Id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
