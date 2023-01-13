import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def all(self) -> None:
        actors_cursor = self._connection.execute(
            f"select id, first_name, last_name from {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"insert into {self.table_name} "
            f"(first_name, last_name) values (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update: int,
               first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"update {self.table_name} "
            f"set first_name = ?, last_name = ? "
            f"where id = {id_to_update}",
            (first_name, last_name)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"delete from {self.table_name} where id = {id_to_delete}"
        )
        self._connection.commit()
