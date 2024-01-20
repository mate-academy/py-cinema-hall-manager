import sqlite3

from models import Actor


class ActorManager:

    def __init__(
            self
    ) -> None:
        self.table_name = "D:/Python_projects/User/py-actor-manager/cinema"
        self.connection_ = sqlite3.connect(f"{self.table_name}")

    # CREATE
    def create(
        self,
        first_name: str,
        last_name: str
    ) -> None:
        self.connection_.execute(
            f"INSERT INTO {self.table_name}"
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection_.commit()

    # READ

    def all(
            self
    ) -> list:
        actors_cursor = self.connection_.execute(
            "SELECT id, first_name, last_name"
            f"FROM {self.table_name} "
        )
        return [Actor(*row) for row in actors_cursor]

    # UPDATE

    def update(
        self,
        id_to_update: int,
        first_name_to_update: str,
        last_name_to_update: str
    ) -> None:
        self.connection_.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id_to_update = ?",
            (first_name_to_update,
             last_name_to_update,
             id_to_update)
        )
        self.connection_.commit()

    # DELETE

    def delete(
        self,
        id_to_delete: int
    ) -> None:
        self.connection_.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self.connection_.commit()
