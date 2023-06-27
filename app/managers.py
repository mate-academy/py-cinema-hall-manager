import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        query = (f"INSERT INTO {self.table_name} (first_name, last_name) "
                 f"VALUES (?, ?)")
        self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self.connection.execute(query)
        return [Actor(*row) for row in cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        query = (f"UPDATE {self.table_name} "
                 f"SET (first_name, last_name) = (?, ?) "
                 f"WHERE id = ?")
        self.connection.execute(query, (first_name, last_name, id_))
        self.connection.commit()

    def delete(self, id_: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.connection.execute(query, (id_,))
        self.connection.commit()
