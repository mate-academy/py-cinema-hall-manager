import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def all(self) -> list:
        actors_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        print(f"actors_cursor: {actors_cursor}")
        actors = []
        for actor in actors_cursor:
            actors.append(Actor(*actor))

        return actors

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO actors (first_name, last_name)\
             VALUES ('{first_name}', '{last_name}')"
        )
        self.connection.commit()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE actors \
            SET first_name = '{first_name}', last_name = '{last_name}' \
            WHERE id = {id}"
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute(
            f"DELETE FROM actors WHERE id = {id}"
        )
        self.connection.commit()
