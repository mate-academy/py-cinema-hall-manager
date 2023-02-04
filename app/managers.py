import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connecting = sqlite3.connect("cinema.db3")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connecting.execute(
            f"INSERT INTO {self.table} "
            "first_name VALUE (?) last_name VALUE (?)",
            (first_name, last_name,)
        )
        self._connecting.commit()

    def all(self) -> list:
        literary_formats_cursor = self._connecting.execute(
            f"SELECT * FROM {self.table}"
        )
        return [Actor(*row) for row in literary_formats_cursor]

    def update(
            self,
            id_to_update: int,
            update_first_name: str,
            update_last_name: str
    ) -> None:
        self._connecting.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ? last_name = ? "
            f"WHERE id = ?",
            (update_first_name, update_last_name, id_to_update,)
        )
        self._connecting.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connecting.execute(
            f"DELETE FROM {self.table} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connecting.commit()
