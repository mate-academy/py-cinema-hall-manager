import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )
        self._connection.commit()

    def all(self):
        authors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        #print(f"authors_cursor: {authors_cursor}")
        return [
            Actor(*row) for row in authors_cursor
        ]

    def update(self, id_to_update: int, first_name: str, last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET format = ? "
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )

        self._connection.commit()


if __name__ == "__main__":
    managers = ActorManager()
    print(managers.all())
