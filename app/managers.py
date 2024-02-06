import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connector = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:

        self._connector.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connector.commit()

    def all(self) -> list[Actor]:
        cursor = self._connector.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in cursor]

    def update(
            self,
            id_to_update: int,
            name_to_update: str,
            surname_to_update: str
    ) -> None:
        self._connector.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (name_to_update, surname_to_update, id_to_update,)
        )
        self._connector.commit()

    def delete(
            self,
            id_to_delete: int
    ) -> None:
        self._connector.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connector.commit()
