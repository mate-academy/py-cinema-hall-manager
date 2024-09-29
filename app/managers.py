import sqlite3
# from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self._initialize_database()

    def _initialize_database(self) -> None:
        self._connection.execute("""CREATE TABLE IF NOT EXISTS actors (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    first_name TEXT NOT NULL,
                                    last_name TEXT NOT NULL)""")
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute("""INSERT INTO actors
                                 (first_name, last_name)
                                 VALUES (?, ?)""",
                                 (first_name, last_name))
        self._connection.commit()

    def all(self) -> None:
        cursor = self._connection.execute("SELECT * FROM actors")
        for row in cursor:
            print(row)
        # return [Actor(*row) for row in cursor]

    def update(self, id: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute("UPDATE actors "
                                 "SET first_name = ?, last_name = ? "
                                 "WHERE id = ?",
                                 (new_first_name,
                                  new_last_name, id))
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id,))
        self._connection.commit()
