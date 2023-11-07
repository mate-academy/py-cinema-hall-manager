import sqlite3

from models import Actor


class ActorManager:
    def __init__(
            self
    ) -> None:
        self._sqlconnection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._sqlconnection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._sqlconnection.commit()

    def all(
            self
    ) -> list[Actor]:
        actors_cursor = self._sqlconnection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            upd_first_name: str,
            upd_second_name: str
    ) -> None:
        self._sqlconnection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (upd_first_name, upd_second_name, id_to_update,)
        )
        self._sqlconnection.commit()

    def delete(
            self,
            id_to_delete: int
    ) -> None:
        self._sqlconnection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._sqlconnection.commit()
