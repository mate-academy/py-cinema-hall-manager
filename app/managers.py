import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"insert into {self.table_name} "
            "(first_name, last_name) values (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"select * from {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"update {self.table_name} "
            "set first_name = ?, last_name = ? "
            "where id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"delete from {self.table_name} "
            "where id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
