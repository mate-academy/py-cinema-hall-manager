import sqlite3


from app.models import Actor


class ActorManager:
    _DB_PATH = "cinema.sqlite"
    _TABLE_NAME = "actors"

    def all(self) -> list[Actor]:
        with sqlite3.connect(self._DB_PATH) as conn:
            actors_cursor = conn.execute(
                f"SELECT * FROM {self._TABLE_NAME}")
            return [Actor(*row) for row in actors_cursor]

    def create(self, _first_name : str, _last_name: str ) -> None:
        with sqlite3.connect(self._DB_PATH) as conn:
            conn.execute(
                f"INSERT INTO {self._TABLE_NAME} VALUES (?, ?)",
                (_first_name, _last_name)
)

    def update(self, _id : int, _first_name : str, _last_name: str ) -> None:
        with sqlite3.connect(self._DB_PATH) as conn:
            conn.execute(
                f"UPDATE {self._TABLE_NAME} "
                f"SET first_name = ?, last_name = ? WHERE id = ?",
                (_first_name, _last_name, _id)
)

    def delete(self, _id : int) -> None:
        with sqlite3.connect(self._DB_PATH) as conn:
            conn.execute(
                f"DELETE FROM {self._TABLE_NAME} WHERE id = ?",
                (_id,)
)
