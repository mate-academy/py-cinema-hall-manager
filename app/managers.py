import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.__connection = sqlite3.connect("cinema.db3")
        self.tabl_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.__connection.execute(
            f"INSERT INTO {self.tabl_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.__connection.commit()

    def all(self) -> list:
        actors = self.__connection.execute(
            f"SELECT * FROM {self.tabl_name}"
        )
        return [Actor(*row) for row in actors]

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str
    ) -> None:
        self.__connection.execute(
            f"UPDATE {self.tabl_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self.__connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.__connection.execute(
            f"DELETE FROM {self.tabl_name} WHERE id = ?",
            (id_to_delete,)
        )
        self.__connection.commit()
