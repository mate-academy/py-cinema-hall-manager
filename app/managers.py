import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._conn = sqlite3.connect(
            "C:/projects/py-actor-manager/cinema.sqlite"
        )
        self.table_name = "actors"

    def all(self) -> list:
        cinema_cursor = self._conn.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in cinema_cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._conn.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._conn.commit()

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._conn.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (first_name, last_name, actor_id)
        )
        self._conn.commit()

    def delete(self, actor_id: int) -> None:
        self._conn.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (actor_id,)
        )
        self._conn.commit()
