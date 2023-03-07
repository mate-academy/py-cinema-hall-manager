import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connected = sqlite3.connect("cinema_db.db3")
        self.table_name = "actors"

    def all(self) -> list:
        actors_data = self._connected.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_data]

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connected.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connected.commit()

    def update(
            self,
            id_to_update: int,
            first_name: str,
            last_name: str,
    ) -> None:
        self._connected.execute(
            f"UPDATE {self.table_name}"
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connected.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connected.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
