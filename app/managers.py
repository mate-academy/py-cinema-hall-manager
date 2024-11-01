import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._conection = sqlite3.connect(r"D:\Games\cinema.db")

    def all(self) -> list:
        actors_data = self._conection.execute(
            "SELECT * FROM actors"
        )

        return [row for row in actors_data]

    def create(self, first_name: str, last_name: str) -> None:
        self._conection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?,?)",
            (first_name, last_name)
        )
        self._conection.commit()

    def update(self, id_: int, new_name: str, new_surname: str) -> None:
        self._conection.execute(
            "UPDATE actors "
            "SET (first_name, last_name) = (?, ?) "
            "WHERE id = ?",
            (id_, new_name, new_surname)
        )
        self._conection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._conection.execute(
            "DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self._conection.commit()
