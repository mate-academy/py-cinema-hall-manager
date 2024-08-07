import sqlite3

from typing import List

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def all(self) -> List[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in cursor
        ]

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(
        self,
        _id: int,
        first_name: str,
        last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id=? ",
            (first_name, last_name, _id)
        )
        self._connection.commit()

    def delete(self, _id: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (_id,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()
    print(manager.all())
