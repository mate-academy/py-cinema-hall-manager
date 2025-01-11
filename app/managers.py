import sqlite3


from app.models import Actor


class ActorManager:
    def __init__(self, db_path: str, table_name: str) -> None:
        self._db_path = db_path
        self._table_name = table_name

        self.conn = sqlite3.connect(self._db_path)

    def all(self) -> list[Actor]:
        cursor = self.conn.execute(f"SELECT * FROM {self._table_name}")
        return [Actor(*row) for row in cursor]

    def create(self, first_name: str, last_name: str) -> None:
        self.conn.execute(
            f"INSERT INTO {self._table_name} VALUES (?, ?)",
            (first_name, last_name)
        )
        self.conn.commit()

    def __del__(self) -> None:
        if self.conn:
            self.conn.close()
