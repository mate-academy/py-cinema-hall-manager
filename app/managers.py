import sqlite3

from models import Actor


class ActorManager:

    def __init__(self, db_name: str) -> None:
        self._connection = sqlite3.connect(db_name)
        self.table_name = "actors"

    def create(self, actor_first_name: str, actor_last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            "VALUES (?, ?)",
            (actor_first_name, actor_last_name)
        )
