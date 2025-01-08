import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        # This method is used to establish a connection to the database.
        # It also creates a table to store actors if it does not exist.
        # The table has three columns: id, first_name, and last_name.
        self.connection = sqlite3.connect('cinema.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS actors
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT,
                            last_name TEXT)''')
        self.connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        # This method is used to create a new actor in the database.
        self.cursor.execute('''INSERT INTO actors (first_name, last_name)
                            VALUES (?, ?)''', (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        # This method is used to retrieve all the actors from the database.
        self.cursor.execute('''SELECT * FROM actors''')
        actors = self.cursor.fetchall()
        return [Actor(*actor) for actor in actors]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        # This method is used to update an actor in the database.
        self.cursor.execute('''UPDATE actors SET first_name = ?, last_name = ?
                            WHERE id = ?''', (first_name, last_name, id))
        self.connection.commit()

    def delete(self, id: int) -> None:
        # This method is used to delete an actor from the database.
        self.cursor.execute('''DELETE FROM actors WHERE id = ?''', (id,))
        self.connection.commit()

    def __del__(self) -> None:
        # This method is used to close the connection to the database.
        self.connection.close()
