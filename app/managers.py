from app.models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")

    table_name = "actors"

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in cursor]

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def update(
            self,
            id_to_update: int,
            first_name_: str,
            last_name_: str) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 f"SET first_name = ?,last_name = ? "
                                 f"WHERE id = ?",
                                 (first_name_, last_name_, id_to_update))
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
