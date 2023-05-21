import sqlite3


class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect("cinema.db3")

    def all(self):
        self.connection.execute("SELECT * FROM actors")

    def create(self, first_name, last_name):
        self.connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def update(self, id_to_update: int, new_first_name, new_last_name):
        self.connection.execute(
            "UPDATE actors SET first_name=?, last_name=? WHERE id=?",
            (new_first_name, new_last_name, id_to_update)
        )
        self.connection.commit()

    def delete(self, id_to_delete):
        self.connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()
