import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"""
            INSERT INTO {self.table} (first_name, last_name) 
            VALUES (?, ?)
""", (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, id_updated: int, first_name: str, last_name: str) -> None:
        self._connection.execute(f"""
        UPDATE {self.table}
        SET first_name = ?, last_name = ? 
        WHERE id = ?
""",
            (first_name, last_name, id_updated)
        )
        self._connection.commit()

    def delete(self, id_delete: int) -> None:
        self._connection.execute(f"""
        DELETE FROM {self.table} 
        WHERE id = ?
""",
            (id_delete,)
        )
        self._connection.commit()
