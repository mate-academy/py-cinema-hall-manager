import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.db")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"""
            INSERT INTO {self.table_name}
            (first_name, last_name) VALUES (?, ?)
            """
            , (first_name, last_name)

        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"""
            SELECT * FROM {self.table_name}
            """
        )
        return [Actor(*row) for row in actor_cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """
            , (last_name, first_name, id_)
        )
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self._connection.execute(
            f"""
            DELETE FROM {self.table_name} WHERE id = ?
            """
            , (id_,)
        )
        self._connection.commit()
