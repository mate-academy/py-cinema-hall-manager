from models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )

        self._connect.commit()

    def all(self) -> list:
        info = self._connect.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in info
        ]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_)
        )

        self._connect.commit()

    def delete(self, id_: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_,)
        )

        self._connect.commit()
