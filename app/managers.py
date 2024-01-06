import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.3db")
        self.table_name = "actor"

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cinema_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )

        return [Actor(*row) for row in cinema_cursor]

    def update(self, id_new: int, fname_new: str, lname_new: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (fname_new, lname_new, id_new)
        )
        self._connection.commit()

    def delete(self, id_del) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_del,)
        )
        self._connection.commit()
