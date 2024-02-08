import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*line) for line in cursor]

    def update(
            self,
            id_actor: int,
            update_first_name: str,
            update_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (update_first_name, update_last_name, id_actor)
        )
        self._connection.commit()

    def delete(self, id_actor: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ? ",
            (id_actor,)
        )
        self._connection.commit()
