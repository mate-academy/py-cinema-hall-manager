import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, actor_id: int, actor_name: str, actor_surname: str
               ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET {actor_name} = ? "
            f"WHERE id = ? ",
            (actor_surname, actor_id,)
        )
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE "
            f"FROM {self.table_name} WHERE id = ? ",
            (actor_id,)
        )
        self._connection.commit()


manager = ActorManager()
manager.update(1, "Asd", "123")
