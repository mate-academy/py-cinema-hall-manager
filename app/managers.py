import sqlite3


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
        actors = self._connection.execute("SELECT * FROM actors")
        self._connection.commit()
        result_list = [str(actor) for actor in actors]
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
