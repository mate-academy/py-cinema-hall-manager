import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actor"
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str) -> None:
        if new_first_name and not new_last_name:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ? "
                f"WHERE id = ? ",
                (new_first_name, id_to_update)
            )

        if new_last_name and not new_first_name:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET last_name = ? "
                f"WHERE id = ? ",
                (new_last_name, id_to_update)
            )

        if new_first_name and new_last_name:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ? "
                f"WHERE id = ?",
                (new_first_name, new_last_name, id_to_update)
            )

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ? ",
            (id_to_delete, )
        )
        self._connection.commit()
