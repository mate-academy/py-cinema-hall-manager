import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")

    def all(self) -> list[Actor]:
        actor_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        return [Actor(*row) for row in actor_cursor]

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )

    def update(
            self,
            id: int,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name=?, last_name=?, id=?",
            (first_name, last_name, id)
        )
        self._connection.commit()

    def delete(self, id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id=?",
            (id,)
        )
        self._connection.commit()
