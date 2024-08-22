import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('cinema.sqlite')
        self.table_name = 'actors'

    def create(self, first_name, last_name) -> None:
        self.connection.execute(
            f"""
            INSERT INTO {self.table_name} (first_name, last_name)
            VALUES (?, ?)
            """,
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list:
        all_actors = self.connection.execute(
            f"""
            SELECT * FROM {self.table_name}
            """
        )

        return [
            Actor(*actor)
            for actor in all_actors
        ]

    def update(
            self,
            id_: int,
            new_first_name: str,
            new_last_name: str,
    ):
        self.connection.execute(
            f"""
            UPDATE {self.table_name}
            SET first_name = ?, last_name = ?
            WHERE id = ?
            """,
            (id_, new_first_name, new_last_name),
        )
        self.connection.commit()

    def delete(self, id_: int) -> None:
        self.connection.execute(
            f"""
            DELETE FROM {self.table_name} 
            WHERE id = ?
            """,
            (id_,)
        )
        self.connection.commit()
