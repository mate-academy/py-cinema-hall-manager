import sqlite3
from models import Actor

class ActorManager:
    def __init__(self):
        self.connection = sqlite3.connect('cinema.db')
        self.table_name = 'actors'

    def create(self, first_name: str, last_name: str):
       self.connection.execute(
           f"INSERT INTO actors (first_name, last_name) VALUES ('{first_name}', '{last_name}')"
       )
        self.connection.commit()

    def select_all(self):
        self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return self.connection.fetchall()

    def update(self, actor: Actor):
        self.connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (actor.first_name, actor.last_name, actor.id)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int):
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self.connection.commit()