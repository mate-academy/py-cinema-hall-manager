import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db")
        self.cinema_table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.cinema_table} (first_name, last_name) "
            "VALUES ((?),(?))",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.cinema_table}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.cinema_table} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.cinema_table} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
