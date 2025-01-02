from models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite3")
        self.table_name = "actors"
        self._create_actors_table()

    def _create_actors_table(self) -> None:
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT, last_name TEXT)"
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        # creates a new entry in the actors table
        # with given properties
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        # returns a list of Actor instances from DB
        db_runner = self._connection.execute(
            f"SELECT id number, first_name name, last_name "
            f"FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in db_runner
        ]

    def update(self, id_to_update: int,
               first_name: str, last_name: str) -> None:
        # updates properties for entry with given id
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        # deletes entry with given id from DB
        self._connection.execute(f"DELETE FROM {self.table_name} "
                                 f"WHERE id = {id}")
        self._connection.commit()
