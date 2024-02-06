import sqlite3

from models import Actor


class ActorManager:
    def __init__(self: any) -> None:
        self._conn = sqlite3.connect('cinema.sqlite')
        self.table_name = 'actor'

    def create(self: any, first_name: str, last_name: str) -> None:
        self._conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f" VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._conn.commit()

    def update(
            self: any,
            id_actor: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._conn.execute(
            f"UPDATE {self.table_name} "
            'SET first_name = ?, last_name = ? WHERE id_ = ? ',
            (new_first_name, new_last_name, id_actor,)
        )
        self._conn.commit()

    def delete(self: any, id_to_delete: int) -> None:
        self._conn.execute(
            f"DELETE FROM {self.table_name} WHERE id_ = ? ",
            (id_to_delete,)
        )
        self._conn.commit()

    def all(self: any) -> any:
        cinema_cursor = self._conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in cinema_cursor
        ]
