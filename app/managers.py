import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

        with self.connection:
            self.connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name}"
                f"("
                f"id INTEGER PRIMARY KEY,"
                f"first_name VARCHAR(63) NOT NULL,"
                f"last_name VARCHAR(63) NOT NULL"
                f")"
            )

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        actor_manager_cursor = self.connection.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )

        return [Actor(*row) for row in actor_manager_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update,)
        )

        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )

        self.connection.commit()
