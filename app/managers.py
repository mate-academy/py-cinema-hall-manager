import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    # CREATE  C
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name}"
            f" (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name, )
        )
        self._connection.commit()

    # RETRIEVE (READ) R
    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    # UPDATE U
    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} SET first_name = ?, last_name = ?"
            f" WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    # DELETE D
    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()

#
# if __name__ == "__main__":
#     manager = ActorManager()
#     # manager.update(
#     #     id_to_update=1,
#     #     new_format="prose"
#     # )
#     manager.delete(id_to_delete=3)
#     print(manager.all())
