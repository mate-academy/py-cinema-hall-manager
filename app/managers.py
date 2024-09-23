import _sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = _sqlite3.connect("./../db/cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> [Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in actors
        ]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_)
        )

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_,)
        )
