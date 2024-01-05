import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*actor) for actor in cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        if first_name and last_name:
            self.connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ?"
                f" WHERE id = {actor_id}",
                (first_name, last_name)
            )
        elif first_name:
            self.connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ? "
                f"WHERE id = {actor_id}",
                (first_name,),
            )
        elif last_name:
            self.connection.execute(
                f"UPDATE {self.table_name} "
                f"SET last_name = ? "
                f"WHERE id = {actor_id}",
                (last_name,),
            )
        self.connection.commit()

    def delete(self, actor_id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = {actor_id}"
        )
        self.connection.commit()
