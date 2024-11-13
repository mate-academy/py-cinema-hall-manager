from models import Actor
import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.connect_ = sqlite3.connect("cinema.sqlite")
        self.tabel_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.connect_.execute(
            f"INSERT INTO {self.tabel_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )

        self.connect_.commit()

    def all(self) -> list:
        info = self.connect_.execute(
            f"SELECT * FROM {self.tabel_name}"
        )

        return [
            Actor(*row) for row in info
        ]

    def update(self, id_: int, first_name: str, last_name: str) -> None:
        self.connect_.execute(
            f"UPDATE {self.tabel_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, id_)
        )

        self.connect_.commit()

    def delete(self, id_: int) -> None:
        self.connect_.execute(
            f"DELETE FROM {self.tabel_name} WHERE id = ?",
            (id_,)
        )

        self.connect_.commit()


database = ActorManager()

database.create("maks", "p")
print(database.all())
