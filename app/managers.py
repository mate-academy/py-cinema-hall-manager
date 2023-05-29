import sqlite3
from typing import List

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def all(self) -> List[Actor]:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def update(
            self, id_to_update: int,
            new_first_name: str = None,
            new_last_name: str = None
    ) -> None:
        update_query = f"UPDATE {self.table_name} SET"
        params = []
        if new_first_name:
            update_query += f" first_name = ?,"
            params.append(new_first_name)

        if new_last_name:
            update_query += f" last_name = ?,"
            params.append(new_last_name)

        update_query = update_query.rstrip(',')

        update_query += f" WHERE id = ?;"
        params.append(id_to_update)
        self._connection.execute(update_query, params)
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        delete_query = f"DELETE FROM {self.table_name} WHERE id=?"
        self._connection.execute(delete_query, (id_to_delete,))
        self._connection.commit()


if __name__ == '__main__':
    manager = ActorManager()
    print(manager.all())

