import sqlite3
from models import Actor


class ActorManager:
    def __init__(self,) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [Actor(*actor) for actor in actors]

    def update(
            self,
            id: int,
            new_first_name: str,
            new_last_name: str
        ) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, "
            f"last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
            f"WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()

    def delete_all(self) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
        )
        self._connection.commit()
