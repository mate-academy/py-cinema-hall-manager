import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connect.commit()

    def all(self):
        cinema_cursor = self._connect.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in cinema_cursor
        ]

    def update(
            self,
            updated_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, updated_id)
        )
        self._connect.commit()

    def delete(self, id_to_del: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_del,)
        )
        self._connect.commit()
