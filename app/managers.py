import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cursor = self._connection.execute(
            "SELECT * FROM " + self.table_name
        )
        return [Actor(*row) for row in cursor]

    def update(self, actor_id: int, column_name: str, new_value: str) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 f"SET {column_name} = ? "
                                 f"WHERE id = ?",
                                 (new_value, actor_id))
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ? ",
            (id_to_delete,))
