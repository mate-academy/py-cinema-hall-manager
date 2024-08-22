import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("./cinema.sqlite")
        self.table_name = "actors"
        self.db_name = "cinema.sqlite"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} VALUES (?, ?, ?) ",
            (None, first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        reader = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in reader]

    def update(self, key: int, f_name: str, l_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name =? "
            f"WHERE id=? ",
            (f_name, l_name, key)
        )
        self._connection.commit()

    def delete(self, key: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id=? ",
            (key,)
        )
