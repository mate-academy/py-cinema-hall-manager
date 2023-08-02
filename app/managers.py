import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name_to_add, last_name_to_add) -> None:  # C
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name,last_name)"
            " VALUES (?,?)",
            (first_name_to_add, last_name_to_add)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:  # R
        return [
            Actor(*row) for row in
            self._connection.execute(
                f"SELECT * from {self.table_name}"
            )
        ]

    def update(self, id_to_update, first_name_upd, last_name_upd)->None:  # U

        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = {id_to_update}",
            (first_name_upd, last_name_upd)
        )
        self._connection.commit()

    def delete(self, id_to_delete):  # D
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE ID = {id_to_delete}"
        )
        self._connection.commit()


if __name__ == '__main__':
    manager = ActorManager()
    manager.create("Bob", "Gross")
    manager.update(7, "w", "dsa")
    for i in range(40,48):
        try:
            manager.delete(i)
        except Exception as e:
            print(e)
    print(manager.all())


# CREATE TABLE actors (
#     id         INTEGER       PRIMARY KEY AUTOINCREMENT,
#     first_name VARCHAR (255),
#     last_name  VARCHAR (255)
# );
