import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._conn = sqlite3.connect("cinema.sqlite")
        self._table_name = "actors"

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._conn.execute(
            f"INSERT INTO "
            f"{self._table_name} (first_name, last_name) "
            f"VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._conn.commit()

    def all(self) -> list:
        actors_cursor = self._conn.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(
            self,
            id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._conn.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id)
        )
        self._conn.commit()

    def delete(self, id_to_delete: int) -> None:
        self._conn.execute(
            f"DELETE "
            f"FROM {self._table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._conn.commit()
