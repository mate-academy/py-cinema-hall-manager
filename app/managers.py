import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sql")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(
            self,
            id_of_object: int,
            setting_first_name: str,
            setting_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (setting_first_name, setting_last_name, id_of_object)
        )
        self._connection.commit()

    def delete(self, id_of_object: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_of_object, )
        )

        # Code below resets the auto-increment counter
        self._connection.execute(
            f"DELETE FROM sqlite_sequence WHERE name = '{self.table_name}'"
        )
        self._connection.commit()
