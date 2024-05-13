import sqlite3

class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"


    def create(self, first_name, last_name) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()
    def all(self) -> None:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}")
        return cursor.fetchall()

    def update(self, id_to_update: int, new_format: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name}"
            f" SET id = ? "
            f" sWHERE id = ? ",
            (id_to_update, new_format)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name}"
            f" WHERE id = ? ",
            (id_to_delete)
        )
        self.connection.commit()