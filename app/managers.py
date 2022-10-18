import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../DB/cinema.db3")
        self._table_name = "actors"

    def create(self, create_first_name: str, create_last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name,last_name) VALUES (?, ?)",
            (create_first_name, create_last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_rows = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [Actor(*row) for row in actors_rows]

    def update(self, id_actor_update: int,
               first_name_update: str,
               last_name_update: str) -> None:

        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (first_name_update, last_name_update, id_actor_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
