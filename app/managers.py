import sqlite3
from models import Actor
import os


class ActorManager:
    def __init__(self) -> None:
        db_path = os.path.join("..", "cinema.sqlite")
        self._connection = sqlite3.connect(db_path)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO actors (first_name, last_name) VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM actors "
        )
        return [Actor(*actor) for actor in actor_cursor]

    def update(self,
               id_to_update: int,
               new_f_name: str,
               new_l_name: str) -> None:
        self._connection.execute(
            f"UPDATE actors "
            "SET (first_name, last_name) = (?, ?) "
            "WHERE id = ? ",
            (new_f_name, new_l_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM actors WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()
