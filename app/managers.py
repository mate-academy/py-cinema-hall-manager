import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.base_table = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name_: str, last_name_: str) -> None:
        self.base_table.execute(
            f"INSERT INTO {self.table_name}"
            "(first_name,last_name)"
            "VALUES (?,?)",
            (
                first_name_,
                last_name_,
            ),
        )
        self.base_table.commit()

    def all(self) -> list:
        actors_cursor = self.base_table.execute(
            f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actors_cursor]

    def update(
        self, id_to_update: int,
            first_name_to_update: str,
            last_name_to_update: str
    ) -> None:
        self.base_table.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (first_name_to_update, last_name_to_update, id_to_update),
        )
        self.base_table.commit()

    def delete(self, id_to_delete: int) -> None:
        self.base_table.execute(
            f"DELETE FROM {self.table_name}"
            "WHERE id = ?",
            (id_to_delete,)
        )
        self.base_table.commit()
