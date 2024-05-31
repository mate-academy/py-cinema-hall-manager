import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.db_name = "cinema.db"
        self.table_name = "actors"
        self.actor_db_connect = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self.actor_db_connect.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?);", (first_name, last_name)
        )
        self.actor_db_connect.commit()

    def all(self) -> list[type(Actor)]:
        return [
            Actor(*actor_item) for actor_item in self.actor_db_connect.execute(
                "SELECT * FROM actors;"
            )
        ]

    def update(self, id_number: int, first_name: str, last_name: str) -> None:
        self.actor_db_connect.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?;", (first_name, last_name, str(id_number))
        )
        self.actor_db_connect.commit()

    def delete(self, id_number: int) -> None:
        self.actor_db_connect.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?;", (str(id_number))
        )
        self.actor_db_connect.commit()
