import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name,last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_rows = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [Actor(*row) for row in actors_rows]

    def update(self, id_upd: int,
               f_name_upd: str,
               l_name_upd: str) -> None:

        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (f_name_upd, l_name_upd, id_upd)
        )
        self._connection.commit()

    def delete(self, id_del: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?",
            (id_del,)
        )
        self._connection.commit()
