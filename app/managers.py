import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "cinema"

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name "
            f"FROM {self.table_name}"
        )

        return [Actor(*row) for row in actors_cursor]

    def create(self,
               first_name: str,
               last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name) VALUES ({first_name}), "
            f"(last_name) VALUES ({last_name})"
        )
        self._connection.commit()

    def update(self,
               id_to_update: int,
               new_name: str,
               new_surname: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = {new_name}, "
            f"last_name = {new_surname} "
            f"WHERE id = {id_to_update}"
        )

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = {id_to_delete}"
        )
