import sqlite3


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
            f"INSERT INTO {self._table_name} "
            "(first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._conn.commit()

    def all(self) -> None:
        actors_cursor = self._conn.execute(
            f"SELECT * FROM {self._table_name}"
        )
        for row in actors_cursor:
            print(row)

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
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._conn.commit()
