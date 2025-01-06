import sqlite3


from models import Actor

class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('cinema_db.sqlite')
        self.table_name = 'actors'
        self._connection.execute("""
            CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
            )
        """)
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute("""
            INSERT INTO actors (first_name, last_name) VALUES (?, ?)
        """, (first_name, last_name))
        self._connection.commit()

    def all(self) -> list:

        actors_cursor = self._connection.execute("""
        SELECT * FROM actors
        """)
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute("""
        UPDATE actors
        SET first_name = ?, last_name = ?
        WHERE id = ?
        """, (id_to_update, new_first_name, new_last_name))

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute("""
        DELETE FROM actors WHERE id = ?
        """, (id_to_delete,))
        self._connection.commit()