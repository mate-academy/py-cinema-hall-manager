import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, second_name) "
            f"VALUES (?,?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, second_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id),
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id =?",
            (id,)
        )
        self._connection.commit()
