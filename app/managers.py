import sqlite3
from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, ft_nm: str, lt_nm: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (ft_nm, lt_nm) VALUES (?, ?)",
            (ft_nm, lt_nm,)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in format_cursor]

    def update(self, id_to_update: int, first_name: str, lt_nm: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, lt_nm = ? "
            "WHERE id = ?",
            (first_name, lt_nm, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
