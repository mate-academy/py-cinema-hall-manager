import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name,last_name)"
            " VALUES (?,?)",
            (first_name, last_name)
        )

        self._connection.commit()

    def all(self) -> list[Actor]:
        return [
            Actor(*row) for row in
            self._connection.execute(
                f"SELECT * from {self.table_name}"
            )
        ]

    def update(
            self,
            id_to_update: int,
            first_name_upd: str,
            last_name_upd: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = {id_to_update}",
            (first_name_upd, last_name_upd)
        )

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE ID = {id_to_delete}"
        )

        self._connection.commit()
