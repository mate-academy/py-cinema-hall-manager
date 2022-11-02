import sqlite3
from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?,?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cursor = self._connection.execute(f"SELECT id, first_name,"
                                          f" last_name FROM {self.table_name}")
        return [Actor(*row) for row in cursor]

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name}"
                                 f" WHERE id = ?",
                                 (id_to_delete,))
        self._connection.commit()

    def update(self, id_to_update: int, name: str = None,
               surname: str = None) -> None:
        if name is not None and surname is not None:
            self._connection.execute(f"UPDATE {self.table_name}"
                                     f" SET first_name = ?,"
                                     f" last_name = ? WHERE id = ?",
                                     (name, surname, id_to_update))
        elif name is None and surname is not None:
            self._connection.execute(f"UPDATE {self.table_name}"
                                     f" SET last_name = ?"
                                     f" WHERE id = ?",
                                     (surname, id_to_update))
        elif name is not None and surname is None:
            self._connection.execute(f"UPDATE {self.table_name}"
                                     f" SET first_name = ? WHERE id = ?",
                                     (name, id_to_update))
        self._connection.commit()
