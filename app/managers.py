import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.__connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.__connection.execute(
            f"INSERT INTO {self.table_name}"
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.__connection.commit()

    def all(self) -> "Actor":
        actors_cursor = self.__connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(
        self,
        id_to_update: int,
        name_to_update: str,
        last_name_to_update: str
    ) -> None:
        self.__connection.execute(
            f"""UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?""",
            (name_to_update, last_name_to_update, id_to_update)
        )
        self.__connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.__connection.execute(
            f"""DELETE FROM {self.table_name}
            WHERE id = ?""",
            (id_to_delete,)
        )
        self.__connection.commit()
