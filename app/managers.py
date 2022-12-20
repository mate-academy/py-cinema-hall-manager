import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, _first_name: str, _last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (_first_name, _last_name) VALUES (?, ?)",
            (_first_name, _last_name,)
        )
        self._connection.commit()

    def all(self) -> object:
        actor_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name"
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(
            self,
            new_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name}"
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (new_first_name, new_last_name, new_id)
        )
        self._connection.commit()

    def delete(self, given_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name}"
            f"WHERE id = ?",
            (given_id,)
        )
        self._connection.commit()
