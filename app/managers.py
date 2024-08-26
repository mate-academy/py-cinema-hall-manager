import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"
        self._create_table()

    def _create_table(self) -> None:
        self._connection.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT, first_name
                TEXT NOT NULL, last_name TEXT NOT NULL)"""
        )
        self._connection.commit()

    def create(
        self,
        first_name: str,
        last_name: str
    ) -> None:
        self._connection.execute(
            f"""INSERT INTO {self.table_name}
            (first_name, last_name)
            VALUES (?, ?)""",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cursor]

    def update(
        self,
        actor_id: int,
        first_name: str,
        last_name: str
    ) -> None:
        self._connection.execute(
            f"""UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?""",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()

    def delete(
            self,
            actor_id: int
    ) -> None:
        self._connection.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
            """,
            (actor_id,)
        )
        self._connection.commit()
