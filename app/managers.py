import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            "INSERT INTO actor (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actor_cursor = self._connection.execute(
            "SELECT * FROM actor"
        )

        return [Actor(*row) for row in actor_cursor]

    def update(self,
               id_to_update: int,
               new_first_name: str,
               new_last_name: str):
        self._connection.execute(
            "UPDATE actor "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            "DELETE FROM actor "
            "WHERE id = ?",
            (id_to_delete, )
        )
        self._connection.commit()
