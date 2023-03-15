import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> list:
        cinema_db = self._connect.execute(
            "SELECT * FROM actors"
        )

        return [Actor(*row) for row in cinema_db]

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_)
        )
        self._connect.commit()

    def delete(self, id_: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_,)
        )
        self._connect.commit()
