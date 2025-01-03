import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO actors (first_name, last_name) "
            f"VALUES ('{first_name}', '{last_name}')"
        )
        self.connection.commit()

    def select_all(self) -> list:
        cursor = self.connection.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        actors = [Actor(id=row[0], first_name=row[1], last_name=row[2])
                  for row in rows]
        return actors

    def update(self, actor: Actor) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (actor.first_name, actor.last_name, actor.id)
        )
        self.connection.commit()

    def delete(self, delete_id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (delete_id,)
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
