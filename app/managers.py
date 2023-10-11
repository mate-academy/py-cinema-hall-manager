import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db")

    def all(self) -> list[Actor]:
        database_cursor = self._connection.execute(
            "SELECT id, first_name, last_name"
            " FROM actor_table")
        return [Actor(*row) for row in database_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actor_table(first_name, last_name)"
            " VALUES (?, ?)",
            (first_name, last_name))
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute("DELETE FROM actor_table WHERE id = ?", (id,))
        self._connection.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self._connection.execute("UPDATE actor_table"
                                 " SET first_name = ?, last_name = ?"
                                 " WHERE id = ?", (first_name, last_name, id))
        self._connection.commit()

    def clear(self) -> None:
        self._connection.execute("DELETE FROM actor_table",)
        self._connection.commit()
