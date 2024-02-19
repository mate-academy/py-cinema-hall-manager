import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.conn = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)", (first_name, last_name,)
        )
        self.conn.commit()

    def all(self):
        actor_cursor = self.conn.execute(F"SELECT * FROM {self.table_name}")
        print(f"actor_cursor: {actor_cursor}")
        for row in actor_cursor:
            print(f"row: {row}")
        return [
            Actor(*row) for row in actor_cursor
        ]

    def update(self, id_to_update: int, first_name: str, last_name: str):
        self.conn.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ? last_name = ? WHERE id = ?", (first_name, last_name, id_to_update,)
        )
        self.conn.commit()

    def delete(self, id_to_delete: int):
        self.conn.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_delete,)
        )
        self.conn.commit()


if __name__ == '__main__':
    manager = ActorManager()
    manager.all()
