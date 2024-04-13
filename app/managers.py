import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema_db.sqlite")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        curr_cursor = self._connection.execute(
            f"select * from {self.table_name}"
        )
        return [Actor(*data) for data in curr_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"insert into {self.table_name} "
            f"(first_name, last_name) values (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_upd: int, new_first_name: str,
               new_last_name: str) -> None:
        self._connection.execute(
            f"update {self.table_name} set "
            f"first_name = ?, last_name = ? "
            f"where id = ?",
            (new_first_name, new_last_name, id_upd)
        )
        self._connection.commit()

    def delete(self, id_del: int) -> None:
        self._connection.execute(
            f"delete from {self.table_name} "
            f"where id = ?",
            (id_del,)
        )
        self._connection.commit()
