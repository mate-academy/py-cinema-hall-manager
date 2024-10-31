import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.db_connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, second_name: str) -> None:
        self.db_connection.execute(
            f"INSERT INTO {self.table_name} (first_name, second_name)"
            f" VALUES (?, ?)",
            (first_name, second_name)
        )

        self.db_connection.commit()

    def read_all(self) -> list:
        list_of_actors = self.db_connection.execute(f"SELECT * FROM"
                                                    f" {self.table_name}")
        return [Actor(*i) for i in list_of_actors]

    def update(self,
               new_first_name: str,
               new_last_name: str,
               id_to_update: int) -> None:
        self.db_connection.execute(
            f"UPDATE {self.table_name}"
            "SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )

        self.db_connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.db_connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self.db_connection.commit()

    def close(self) -> None:
        self.db_connection.close()