import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name, )
        )
        self.conn.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actor_cursor]

    def update(
            self,
            id_actor: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self.conn.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id_ = ? ",
            (new_first_name, new_last_name, id_actor,)
        )
        self.conn.commit()

    def delete(self, id_to_delete: int) -> None:
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id_ = ? ",
            (id_to_delete,)
        )
        self.conn.commit()
