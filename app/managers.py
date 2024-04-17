import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"insert into {self.table_name}"
            f"(first_name, last_name) values (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self) -> [Actor]:
        cinema_cursor = self._connection.execute(
            f"select * from {self.table_name}"
        )
        return [
            Actor(*row) for row in cinema_cursor
        ]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"update {self.table_name} "
            f"set first_name = ?, last_name = ? where id = ?",
            (first_name, last_name, id_,)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"delete from {self.table_name} where id = ?",
            (id_,)
        )
        self._connection.commit()
