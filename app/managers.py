import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('cinema_db.sqlite')
        self._cursor = self._connection.cursor()
        self.table_name = 'actors'

    def create(self, first_name, last_name):
        self._cursor.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

        self._connection.commit()

    def all(self):
        actor_cursor = self._cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actor_cursor]

    def update(self, actor_id, first_name, last_name):
        self._cursor.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, actor_id)
        )

        self._connection.commit()

    def delete(self, actor_id):
        self._cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (actor_id,)
        )

        self._connection.commit()
