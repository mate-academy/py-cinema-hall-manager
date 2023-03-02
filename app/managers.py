import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name_, last_name_,)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            "SELECT *"
            f"FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self, id_to_update, first_name_, last_name_):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, "
            "last_name = ? "
            "WHERE id = ?",
            (first_name_, last_name_, id_to_update,)
        )
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(f"DELETE FROM {self.table_name} "
                                 "WHERE id = ?", (id_to_delete,)
                                 )
        self._connection.commit()


if __name__ == '__main__':
    manager = ActorManager()
    manager.delete(8)
    print(manager.all())
