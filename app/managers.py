import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection_ = sqlite3.connect("cinema")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        actor_cursor = self.connection_.execute(
            f"SELECT * FROM {self.table_name}")

        return [Actor(*row) for row in actor_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self.connection_.execute(f"INSERT INTO {self.table_name}"
                                 f" (first_name, last_name) VALUES (?,?)",
                                 (first_name, last_name))
        self.connection_.commit()

    def update(self, id_update: int,
               first_name_new: str, last_name_new: str) -> None:
        self.connection_.execute(f"UPDATE {self.table_name} "
                                 f"SET first_name = ?,"
                                 f" last_name = ? WHERE id = ?",
                                 (first_name_new, last_name_new, id_update))
        self.connection_.commit()

    def delete(self, id_delete: int) -> None:
        self.connection_.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_delete,))
        self.connection_.commit()
