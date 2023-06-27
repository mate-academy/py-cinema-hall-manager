import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self,
               first_name: str,
               last_name: str) -> None:
        query = f"""
        INSERT INTO {self.table_name}
        (first_name, last_name) VALUES (?, ?)
        """
        self.connection.execute(query, (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        query = f"SELECT * FROM {self.table_name}"
        actors_cursor = self.connection.execute(query)
        return [Actor(*row) for row in actors_cursor]

    def update(self,
               id_to_update: int,
               first_name: str,
               last_name: str) -> None:

        query = f"""
                UPDATE {self.table_name}
                SET first_name = ?,
                    last_name = ?
                WHERE id = ?
                """
        self.connection.execute(query, (first_name, last_name, id_to_update))
        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        query = f"""
                DELETE FROM {self.table_name}
                WHERE id = ?
                """
        self.connection.execute(query, (id_to_delete, ))
