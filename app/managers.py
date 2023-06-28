import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("../cinema.sqlite")

    def create(self, first_name, last_name):
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        all_content_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in all_content_cursor]

    def update(self, id_, new_first_name, new_last_name):
        self._connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_)
        )
        self._connection.commit()

    def delete(self, id_):
        self._connection.execute(
            "DELETE FROM actors "
            "WHERE id = ?",
            (id_,)
        )
        self._connection.commit()
