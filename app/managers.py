import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            " (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT *  FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update: int | str, **kwargs) -> None:
        set_query = ", ".join(f"{key} = ?" for key in kwargs.keys())
        values = tuple(kwargs.values()) + (id_to_update,)
        self._connection.execute(
            f"UPDATE {self.table_name}"
            f" SET {set_query}"
            f" WHERE id = ?",
            values
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name}"
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
