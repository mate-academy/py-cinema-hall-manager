from sqlite3 import connect

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = connect("cinema.sqlite")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*actor)
            for actor in actors_cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
