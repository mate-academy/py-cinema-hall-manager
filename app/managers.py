import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.sqlite")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            "SELECT * FROM {self._table_name}",
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f'UPDATE {self._table_name} '
            f'SET first_name=?, last_name=? WHERE id=?',
            (first_name, last_name, actor_id)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f'DELETE FROM {self._table_name} '
            f'WHERE id=?',
        )
        self._connection.commit()
