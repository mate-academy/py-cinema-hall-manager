import sqlite3


class ActorManager:

    def __init__(self) -> None:
        self.connection = sqlite3.connect("../cinema.sqlite")
        self._table_name = "actors"

    def all(self) -> list:
        data = self.connection.execute(
            f"SELECT * FROM {self._table_name} "
        )

        return [actor for actor in data]

    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self._table_name} VALUES (NULL, ?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self._table_name} SET first_name=?, "
            f"last_name=? WHERE actor_id=?",
            (first_name, last_name, id)
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self._table_name} WHERE actor_id=?",
            (id,)
        )
        self.connection.commit()
