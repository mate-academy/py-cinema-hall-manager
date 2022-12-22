import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("Cinema_db.db3")
        self.table_name = "actors"

    def all(self):
        cinema_data_info = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(id=row[0],
                      first_name=row[1],
                      last_name=row[2])
                for row in cinema_data_info]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (first_name, last_name, id_)

        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_,)
        )
        self._connection.commit()
