import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("app/cinema.sqlite3")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) VALUES (?);",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name};")
        return [Actor(*row) for row in actors_cursor]

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass


db = ActorManager()
print(db.all())
