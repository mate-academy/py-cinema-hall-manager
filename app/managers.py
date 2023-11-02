import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        cursor = self._connection.execute("SELECT * "
                                          "FROM actors")

        return [Actor(*row) for row in cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self,
               actor_id: int,
               first_name: str = None,
               last_name: str = None) -> None:
        if first_name is not None:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ? "
                f"WHERE id = ?",
                (first_name, actor_id)
            )
        if last_name is not None:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET last_name = ? "
                f"WHERE id = ?",
                (last_name, actor_id)
            )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ?",
            (actor_id, )
        )
        self._connection.commit()
