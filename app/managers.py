import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.db_table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.db_table} (first_name, last_name) "
            f"VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self.db_table}"
        )
        return [Actor(*actor) for actor in actors]

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.db_table} WHERE id = ?", (actor_id,)
        )

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.db_table} SET first_name = ?, last_name = ? "
            f"WHERE id = ?", (first_name, last_name, actor_id)
        )
        self._connection.commit()
