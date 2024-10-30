import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute("INSERT INTO actors (first_name, last_name)"
                                " VALUES (?, ?)", (first_name, last_name))
        self.connection.commit()

    def all(self) -> list[Actor]:
        actor_cursor = self.connection.execute("SELECT * FROM actors")
        return [Actor(*row) for row in actor_cursor]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute("UPDATE actors SET  first_name = ?, "
                                "last_name = ? WHERE id = ?",
                                (first_name, last_name, actor_id))
        self.connection.commit()

    def delete(self, actor_id : int, ) -> None:
        self.connection.execute("DELETE from actors WHERE id = ?", (actor_id,))
        self.connection.commit()
