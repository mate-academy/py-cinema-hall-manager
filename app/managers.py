import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, *args, **kwargs) -> None:
        if args:
            f_name = args[0]
            l_name = args[1]
        if kwargs:
            f_name = kwargs.get("first_name")
            l_name = kwargs.get("last_name")
        else:
            return
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (f_name, l_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_name_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_name_cursor]

    def update(
            self, id_for_update: int,
            new_f_name: str,
            new_l_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_f_name, new_l_name, id_for_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = {id_to_delete}"
        )
        self._connection.commit()
