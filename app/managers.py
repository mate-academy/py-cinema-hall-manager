import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinama.db3")
        self.table_name = "actors1123123123131231231"

        with self._connection:
            self._connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} "
                "("
                "id INTEGER PRIMARY KEY, "
                "first_name VARCHAR(63) NOT NULL, "
                "last_name VARCHAR(63) NOT NULL"
                ")"
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"INSERT INTO {self.table_name} (first_name, last_name) "
                f"VALUES (?, ?)",
                (first_name, last_name),
            )

    def all(self) -> list[Actor]:
        data_cursor = self._connection.execute(
            f"SELECT * " f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in data_cursor]

    def update(
        self,
        id_to_update: int,
        first_name_: str,
        last_name_: str,
    ) -> None:
        with self._connection:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? "
                f"WHERE id = ?",
                (first_name_, last_name_, id_to_update),
            )

    def delete(self, id_to_delete: int) -> None:
        with self._connection:
            self._connection.execute(
                f"DELETE FROM {self.table_name} " f"WHERE id = ?",
                (id_to_delete,),
            )

    def make_table_clear(self) -> None:
        with self._connection:
            self._connection.execute(f"DELETE FROM {self.table_name}")
