import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"
        self._create_table()

    def _create_table(self) -> None:
        create_table = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
        id INTEGER PRIMARY KEY,
        first_name TEXT, last_name TEXT
        );"""
        cursor = self._connection.cursor()
        cursor.execute(create_table)
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            " VALUES(?, ?)",
            (first_name, last_name),
        )

        self._connection.commit()

    def all(self) -> list[Actor]:
        actors_data = self._connection.execute("SELECT * FROM actors")
        return [Actor(*row) for row in actors_data]

    def update(
        self, id_to_update: int, new_first_name: str, new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ?"
            " WHERE id = ?",
            (new_first_name, new_last_name, id_to_update),
        )

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (id_to_delete,)
        )

        self._connection.commit()
