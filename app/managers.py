import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)"
            (first_name, last_name)
        )

    def all(self) -> list[Actor]:
        actors_cursore = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in actors_cursore]

    def update(
            self, first_name_update: str,
            last_name_update: str, id_update: int
    ) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ? AND last_name = ? "
            "WHERE id = ?",
            (first_name_update, last_name_update, id_update)
        )
        self._connection.commit()

    def delete(self, actor_id: str) -> None:
        self._connection.execute(
            "DELETE FROM actors "
            "WHERE id = ? "
            (actor_id,)
        )
        self._connection.commit()
