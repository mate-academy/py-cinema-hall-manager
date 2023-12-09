import sqlite3
from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("db_path")
        self.table_name = "actors"

    def create(self, format_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )
        self._connection.commit()

    def all(self) -> List:
        actor_data_cursor = self._connection.execute(
            "SELECT id, format FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_data_cursor]

    def update(self, id_to_update: int, new_format: str) -> None:
        self._connection.execute(
            f"UPDATE{self.table_name} "
            "SET format = ?"
            "WHERE id = ?",
            (new_format, id_to_update)
        )
        self._connection.commit()

    def __delete__(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM{self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()


# if __name__ == "__main__":
#     manager = ActorManager()
#     manager.all()
#     manager.update(
#         id_to_update=1,
#         new_format="prose"
#     )
#     manager.delete(id_to_delete=3)
#     print(manager.all())
