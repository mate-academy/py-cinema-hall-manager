import sqlite3
from typing import List
from models import Actor


class ActorManager:

    def __init__(self) -> None:
        # Connection to DB
        self.connection = sqlite3.connect("app/sinima.sqlite")
        self.cursor = self.connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        # add new data
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> List[Actor]:
        # get all data
        self.cursor.execute("SELECT * FROM actors")
        records = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1], last_name=row[2]) for row
                in records]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        # update data
        self.cursor.execute(
            "UPDATE actors SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        # delete data
        self.cursor.execute("DELETE FROM actors WHERE id=?", (actor_id,))
        self.connection.commit()

    def __del__(self) -> None:
        # Close connection with DB to deleting
        self.connection.close()
