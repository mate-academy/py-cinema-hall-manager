import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("../cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self.conn.execute(
            f"SELECT * "
            f"FROM {self.table}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self,
               id_to_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.conn.execute(
            f"UPDATE {self.table}"
            f" SET first_name = ?,"
            f" last_name =? "
            f"WHERE id = ?",
            (id_to_update, new_first_name, new_last_name)
        )
        self.conn.commit()

    def delete(self, id_to_delete: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table}"
            f" WHERE id = ?",
            (id_to_delete,)
        )
        self.conn.commit()
