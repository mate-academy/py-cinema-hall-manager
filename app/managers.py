import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema")
        self.table_name = "actors"

        with self._connection:
            self._connection.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} "
                "("
                "id INTEGER PRIMARY KEY, "
                "first_name VARCHAR(63) NOT NULL, "
                "last_name VARCHAR(63) NOT NULL"
                ")"
            )

    def create(self, first_name: str, last_name: str) -> None:
        with self._connection:
            self._connection.execute(
                f"INSERT INTO {self.table_name} "
                f"(first_name, last_name) VALUES (?, ?)",
                (first_name, last_name),
            )

    def all(self) -> list:
        with self._connection:
            actors_cursor = self._connection.execute("SELECT * FROM actors")

        return [Actor(*row) for row in actors_cursor]

    def update(
        self, id_to_update: int, new_first_name: str, new_last_name: str
    ) -> None:
        with self._connection:
            self._connection.execute(
                f"UPDATE {self.table_name} "
                f"SET first_name = ?, last_name = ?"
                f"WHERE id = ?",
                (new_first_name, new_last_name, id_to_update),
            )

    def delete(self, id_to_delete: int) -> None:
        with self._connection:
            self._connection.execute(
                f"DELETE FROM {self.table_name} "
                f"WHERE id = ?", (id_to_delete,)
            )

    def clear(self) -> None:
        with self._connection:
            self._connection.execute(f"DROP TABLE {self.table_name}")

            self._connection.execute(
                f"CREATE TABLE {self.table_name} ("
                "    id         INTEGER    PRIMARY KEY AUTOINCREMENT"
                "                          UNIQUE"
                "                          NOT NULL,"
                "    first_name TEXT (255),"
                "    last_name  TEXT (255) "
                ")"
            )


if __name__ == "__main__":
    manager = ActorManager()
    print(manager.all())
