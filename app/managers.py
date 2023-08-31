import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._conection = sqlite3.connect("../cinema")
        self.table_name = "actors"

    def all(self) -> list[Actor]:
        all_users = self._conection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in all_users]

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._conection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._conection.commit()

    def update(
            self,
            id_actor: int,
            first_name: str,
            last_name: str

    ) -> None:
        self._conection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_actor)
        )
        self._conection.commit()

    def delete(self, id_actor: int) -> None:
        self._conection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_actor, )
        )
        self._conection.commit()

    def print_(self) -> None:
        print(self._conection)


if __name__ == "__main__":
    am = ActorManager()
    am.update(1, "Sania", "Sanich ")
    print(am.print_())
