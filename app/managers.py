import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, second_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self.table_name} "
                                 f"(first_name, second_name) VALUES (?, ?)",
                                 (first_name, second_name))
        self._connection.commit()

    def all(self) -> list:
        actors_table = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_table]

    def update(self, id_to_update: int,
               new_first_name: str, new_second_name: str) -> None:
        self._connection.execute(f"UPDATE {self.table_name} "
                                 f"SET first_name = ?, second_name = ?"
                                 f"WHERE id = ?",
                                 (new_first_name,
                                  new_second_name,
                                  id_to_update))
        self._connection.commit()

    def delete(self, id_delete: int) -> None:
        self._connection.execute(f"DELETE FROM {self.table_name} WHERE id = ?",
                                 (id_delete,))
        self._connection.commit()
