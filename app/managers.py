import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connect = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def create(
        self,
        first_name: str,
        last_name: str
    ) -> None:
        self._connect.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) "
            "VALUES (?, ?) ",
            (first_name, last_name),
        )
        self._connect.commit()

    def update(
        self,
        id_to_update: int,
        new_first_name: str,
        new_last_name: str,
    ) -> None:
        self._connect.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, id_to_update),
        )
        self._connect.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connect.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ? ",
            (id_to_delete,),
        )
        self._connect.commit()

    def all(self) -> [Actor]:
        actor_cursor = self._connect.execute(
            f"SELECT * "
            f"FROM {self.table_name}"
        )

        return [Actor(*actor) for actor in actor_cursor]

    def get(self, id_to_get: int) -> Actor:
        actor_cursor = self._connect.execute(
            f"SELECT * "
            f"FROM {self.table_name} "
            f"WHERE id = ? ",
            (id_to_get,),
        )
        actor_cursor = actor_cursor.fetchone()

        return Actor(*actor_cursor)
