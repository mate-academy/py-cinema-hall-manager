import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db3")

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES(?, ?)",
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self) -> list:
        cursor = self.connection.execute("SELECT * FROM actors")
        return [Actor(*actor) for actor in cursor]

    def update(
        self, id_to_change: int, first_name: str = None, last_name: str = None
    ) -> None:
        if first_name and last_name:
            self.connection.execute(
                "UPDATE actors SET first_name = ?, last_name = ?"
                f" WHERE id = {id_to_change}",
                (first_name, last_name),
            )
        elif first_name:
            self.connection.execute(
                f"UPDATE actors SET first_name = ? WHERE id = {id_to_change}",
                (first_name,),
            )
        elif last_name:
            self.connection.execute(
                f"UPDATE actors SET last_name = ? WHERE id = {id_to_change}",
                (last_name,),
            )
        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE FROM actors WHERE id = {id_to_delete}"
        )
        self.connection.commit()
