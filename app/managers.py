import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"""INSERT INTO {self.table_name}
             (first_name, last_name) VALUES (?, ?) """,
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        literary_format_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in literary_format_cursor]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"""UPDATE {self.table_name}
             SET first_name=?, last_name=?
             WHERE id = ?""",
            (first_name, last_name, id_)
        )
        self.connection.commit()

    def delete(self, id_: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_,)
        )
        self.connection.commit()

    def clear_db(self) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name}"
        )
        self.connection.commit()
