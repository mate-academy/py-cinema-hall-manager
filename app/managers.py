import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    # CREATE - C
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    # RETRIEVE - R
    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_cursor
        ]

    # UPDATE - U
    def update(self, id_to_update: int,
               first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    # DELETE - D
    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,),
        )
        self._connection.commit()


# if __name__ == "__main__":
#       manager = ActorManager()
#       manager.create("Mykola", "Kutia")
# #      manager.update(3, "Ivanna", "Yybka")
# #      manager.delete(1)
# #      manager.all()
#       print(manager.all())
