import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.__connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.__connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.__connection.commit()

    def all(self) -> list:
        actor_cursor = self.__connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name} ")

        return [Actor(*row) for row in actor_cursor]

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self.__connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self.__connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.__connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self.__connection.commit()
