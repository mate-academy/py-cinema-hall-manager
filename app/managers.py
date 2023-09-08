from models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

        with self._connection:
            self._connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self._table_name} "
                "("
                "id INTEGER PRIMARY KEY, "
                "first_name VARCHAR(63) NOT NULL, "
                "last_name VARCHAR(63) NOT NULL"
                ")"
            )

    def all(self) -> None:
        actor_manager_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self._table_name}"
        )

        return [Actor(*row) for row in actor_manager_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name)"
            f"VALUES (?,?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(
            self,
            id_search: int,
            upd_first_name: str,
            upd_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (upd_first_name, upd_last_name, id_search)
        )
        self._connection.commit()

    def delete(self, id_search: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (id_search,)
        )
        self._connection.commit()
