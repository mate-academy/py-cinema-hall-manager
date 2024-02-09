import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = (sqlite3.connect("../app/cinema.sqlite"))
        self._cursor = self._connection.cursor()
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT "
            f"INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )

        self._connection.commit()

    def all(self) -> list[Actor]:
        self._cursor.execute(f"SELECT * "
                             f"FROM {self.table_name}")
        return [
            Actor(*row) for row in self._cursor.fetchall()
        ]

    def delete(self, id_del: int) -> None:
        self._cursor.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ?",
            (id_del, )
        )
        self._connection.commit()

    def update(self, update_id: int, name: str, surname: str) -> None:
        self._cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (update_id, name, surname)
        )
        self._connection.commit()
