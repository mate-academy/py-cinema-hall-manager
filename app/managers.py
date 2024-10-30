import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("app/cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*actor) for actor in actors]

    def update(self, id_update: int, first_name: str, last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (first_name, last_name, id_update)
        )

        self._connection.commit()

    def delete(self, id_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_delete,)
        )

        self._connection.commit()
