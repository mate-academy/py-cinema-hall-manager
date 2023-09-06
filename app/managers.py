import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinama.db3")
        self.table_name = "actors"

        if not self.table_exists():
            self.create_table()

    def table_exists(self) -> bool:
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (self.table_name,),
        )
        return cursor.fetchone() is not None

    def create_table(self) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            f"CREATE TABLE {self.table_name} ("
            f"id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name varchar(63), "
            f"last_name INTEGER)"
        )

        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        data_cursor = self._connection.execute(
            f"SELECT * " f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in data_cursor]

    def update(
        self, first_name_: str, last_name_: str, id_to_update: int
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name_, last_name_, id_to_update),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} " f"WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()

    def make_table_clear(self) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name}")
        self._connection.commit()
