import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema_db.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()
