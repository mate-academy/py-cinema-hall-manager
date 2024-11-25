import sqlite3
from models import Actor

class ActorManager:
    def __init__(self, db_name="cinema.db"):
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def create(self, first_name, last_name):
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def all(self):
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        return [Actor(id=row["id"], first_name=row["first_name"], last_name=row["last_name"]) for row in rows]

    def update(self, actor_id, first_name=None, last_name=None):
        if first_name:
            self.cursor.execute(
                "UPDATE actors SET first_name = ? WHERE id = ?", (first_name, actor_id)
            )
        if last_name:
            self.cursor.execute(
                "UPDATE actors SET last_name = ? WHERE id = ?", (last_name, actor_id)
            )
        self.connection.commit()

    def delete(self, actor_id):
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()