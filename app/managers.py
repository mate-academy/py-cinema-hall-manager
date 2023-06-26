import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(self, input_id: int,
               input_first_name: str = None,
               input_last_name: str = None) -> None:

        if input_first_name and not input_last_name:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ? "
                f"WHERE id = ?",
                (input_id, input_first_name,)
            )

        if input_last_name and not input_first_name:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET last_name = ? "
                f"WHERE id = ?",
                (input_id, input_last_name,)
            )

        if input_last_name and input_first_name:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? "
                f"WHERE id = ?",
                (input_id, input_first_name, input_last_name,)
            )

    def delete(self, input_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (input_id,)
        )
