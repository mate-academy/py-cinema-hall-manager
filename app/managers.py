import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema")
        self.table = "actors"

    @staticmethod
    def check_name(first_name: str, last_name: str) -> list:
        if isinstance(first_name and last_name, str):
            return [name.capitalize() for name in [first_name, last_name]]
        else:
            raise TypeError("Name must be string")

    def create(self, first_name: str, last_name: str) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table} "
            "(first_name, last_name) "
            "VALUES (?, ?)",
            (*self.check_name(first_name, last_name),)
        )
        self._connect.commit()

    def all(self) -> list:
        cursor = self._connect.execute(
            f"SELECT id, first_name, last_name FROM {self.table};"
        )
        return [Actor(*actor) for actor in cursor]

    def update(
            self,
            actor_id: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connect.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (
                *self.check_name(new_first_name, new_last_name),
                actor_id,
            )
        )
        self._connect.commit()

    def delete(self, actor_id: int) -> None:
        self._connect.execute(
            f"DELETE FROM {self.table} WHERE id = {actor_id}"
        )
        self._connect.commit()
