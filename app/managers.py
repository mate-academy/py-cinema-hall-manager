import sqlite3
from models import Actor


class TableRedactorContextManager:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def __enter__(self) -> sqlite3.Connection:
        return self.connection

    def __exit__(
        self, exc_type: type(Exception), exc_val: Exception, exc_tb: str
    ) -> None:
        self.connection.commit()
        if exc_type is not None:
            self.connection.close()


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.sqlite")

    def create(self, input_first_name: str, input_last_name: str) -> None:
        with TableRedactorContextManager(self._connection) as redactor:
            sql = "INSERT INTO actors (first_name, last_name) VALUES (?, ?);"
            redactor.execute(sql, (input_first_name, input_last_name))

    def all(self) -> list[Actor]:
        sql = "SELECT * FROM actors;"
        cursor = self._connection.execute(sql)
        return [Actor(*raw) for raw in cursor]

    def update(
        self, input_id: int, input_first_name: str, input_last_name: str
    ) -> None:
        with TableRedactorContextManager(self._connection) as redactor:
            sql = (
                "UPDATE actors "
                "SET first_name = ?, last_name = ? "
                "WHERE id = ?;"
            )
            data = (input_first_name, input_last_name, input_id)
            redactor.execute(sql, data)

    def delete(self, input_id: int) -> None:
        with TableRedactorContextManager(self._connection) as redactor:
            sql = "DELETE FROM actors WHERE id = ?"
            redactor.execute(sql, (input_id,))
