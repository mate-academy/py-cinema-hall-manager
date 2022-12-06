import sqlite3
from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self._name_table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._name_table} "
            f"(first_name, last_name) VALUES(?,?)",
            (first_name, last_name)
        )

        self._connection.commit()

    def all(self) -> list:
        cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self._name_table}"
        )

        return [Actor(*row) for row in cursor]

    def update(self, id_: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._name_table} "
            f"SET (first_name, last_name) = (?,?)"
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_)
        )
        self._connection.commit()

    def delete(self, id_del: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._name_table} "
            f"WHERE id = ?",
            (id_del,)
        )
        self._connection.commit()
