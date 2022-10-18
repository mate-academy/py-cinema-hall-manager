import sqlite3

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self._table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(f"INSERT INTO {self._table} "
                                 f"(first_name, last_name)"
                                 " VALUES (?, ?)", (first_name, last_name))
        self._connection.commit()

    def all(self) -> list:
        actor_line = self._connection.execute(f"SELECT * FROM {self._table}")
        result_list = [Actor(*filed) for filed in actor_line]
        return result_list

    def update(self,
               id_actor: int,
               first_name_new: str,
               last_name_new: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (first_name_new, last_name_new, id_actor)
        )
        self._connection.commit()

    def delete(self, id_actor: int) -> None:
        self._connection.execute(f"DELETE FROM {self._table} "
                                 "WHERE id = ?", (id_actor,))
        self._connection.commit()
