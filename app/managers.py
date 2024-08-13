import sqlite3


class ActorManager:

    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self,) -> list:
        actor_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        self.connection.commit()
        rows = []
        for row in actor_cursor:
            rows.append(row)
        return rows

    def update(self, id_to_update: int, first_name: str, last_name: str,) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_to_update,)
        )
        self.connection.commit()

    def delete(self, first_name: str) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE first_name = ?",
            (first_name,)
        )
        self.connection.commit()
