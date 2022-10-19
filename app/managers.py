import sqlite3

from models import Actor


# CRUD - the four basic functions that models should be able to do...
class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.db3")
        self._table_name = "actors"

    # C (CREATE)
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name, )
        )
        self._connection.commit()

    # R (RETRIEVE / READ)
    def all(self) -> list:
        actors_cursor = \
            self._connection.execute(
                f"SELECT id, first_name, last_name "
                f"FROM {self._table_name}"
            )
        return [Actor(*row) for row in actors_cursor]

    # U (UPDATE)
    def update(self, id_to_update: int,
               first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update, )
        )
        self._connection.commit()

    # D (DELETE)
    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()

    # EXTRA
    # ANALOG TRUNCATE (for SQLite)
    def truncate(self) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name}"
        )
        self._connection.commit()
        self._connection.execute("VACUUM")
        self._connection.commit()
