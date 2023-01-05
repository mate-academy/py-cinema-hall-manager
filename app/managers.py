import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self,
               first_name: str,
               last_name: str
               ) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connect.commit()

    def all(self) -> any:
        return self._connect.execute(
            "SELECT * FROM actors"
        )

    def update(self,
               id_to_update: int,
               new_last_name: str,
               new_first_name: str
               ) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET last_name = ?, first_name = ?"
            "WHERE id = ?",
            (new_last_name, new_first_name, id_to_update)
        )
        self._connect.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connect.commit()
