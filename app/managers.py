import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection_ = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection_.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection_.commit()

    def all(self) -> list:
        actor_cursor = self.connection_.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(
            self,
            update_id: int,
            new_actor_first_name: str,
            new_actor_last_name: str
    ) -> None:
        self.connection_.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_actor_first_name, new_actor_last_name, update_id)
        )
        self.connection_.commit()

    def delete(self, delete_id: int) -> None:
        self.connection_.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = {delete_id}"
        )
        self.connection_.commit()
