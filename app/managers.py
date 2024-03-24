import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"
        self._connection.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            );
        """)
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors = self._connection.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actors]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        query = (f"UPDATE {self.table_name} SET first_name = ?, last_name = ? "
                 f"WHERE id = ?")
        self._connection.execute(query, (first_name, last_name, actor_id))
        self._connection.commit()

    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (actor_id,))
        self._connection.commit()
