import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.sqlite")
        self.table_name = "actors"

    def create_table(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def read_table(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update_actor(
            self,
            id_to_update: int,
            new_actor_fn: str,
            new_actor_ln: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? "
            f"WHERE id=?",
            (new_actor_fn, new_actor_ln, id_to_update)
        )
        self._connection.commit()

    def delete_actor(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id_to_delete,)
        )
        self._connection.commit()
