import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_manager_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name};"
        )
        return [
            Actor(*actor) for actor in actor_manager_cursor.fetchall()
        ]

    def update(self, id_to_update: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            f"where id=?",
            (id_to_delete,)
        )
        self._connection.commit()

    def delete_all(self) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
        )
        self._connection.commit()

    def reset(self) -> None:
        self._connection.execute(
            f"VACUUM"
        )
        self._connection.commit()
