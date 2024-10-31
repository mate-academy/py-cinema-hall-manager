import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self._connection = sqlite3.connect(self._db_name)
        self._create_table()

    def _create_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """
        with self._connection:
            self._connection.execute(query)

    def create(self, first_name: str, last_name: str) -> str:
        query = """
        INSERT INTO actors (first_name, last_name)
        VALUES (?, ?);
        """
        with self._connection:
            cursor = self._connection.execute(query, (first_name, last_name))
            return cursor.lastrowid

    def all(self) -> list:
        query = "SELECT * FROM actors;"
        with self._connection:
            cursor = self._connection.execute(query)
            return [Actor(id=row[0],
                    first_name=row[1],
                    last_name=row[2])
                    for row in cursor.fetchall()]

    def update(self,
               actor_id: int,
               first_name: str,
               last_name: str) -> None:
        query = """
        UPDATE actors
        SET first_name = ?, last_name = ?
        WHERE id = ?;
        """
        with self._connection:
            self._connection.execute(query, (first_name, last_name, actor_id))

    def delete(self, actor_id: int) -> None:
        query = "DELETE FROM actors WHERE id = ?;"
        with self._connection:
            self._connection.execute(query, (actor_id,))

    def close(self) -> None:
        self._connection.close()
