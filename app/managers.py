import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("actors.db")
        self.table_name = "actors"
        self.connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            f"(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)"
        )
        self.connection.commit()

    def create(self, **kwargs) -> None:
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list:
        actor_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, actor_id: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (new_first_name, new_last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (actor_id,)
        )
        self.connection.commit()
