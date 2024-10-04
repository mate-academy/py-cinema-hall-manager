import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self.connection = sqlite3.connect("cinema.db")
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> Actor:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
        actor_id = self.cursor.lastrowid
        return Actor(id=actor_id, first_name=first_name, last_name=last_name)

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1],
                      last_name=row[2]) for row in rows]

    def update(self, actor_id: int, first_name: str,
               last_name: str) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} SET first_name = ?, "
            f" last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?",
                            (actor_id,))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
