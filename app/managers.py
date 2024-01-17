import mysql.connector
from app.models import Actor


class ActorManager:
    def __init__(self):
        self._connection = mysql.connector.connect(
            host="127.0.0.2",
            user="root",
            password="123456",
            database="cinema"
        )
        self.cursor = self._connection.cursor()
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name)"
            "VALUES (%s, %s)",
            (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM ACTORS")
        return [Actor(*row) for row in self.cursor.fetchall()]

    def update(self, id_: int, first_name: str, last_name: str, ) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = %s, last_name = %s "
            "WHERE id = %s",
            (first_name, last_name, id_))
        self._connection.commit()

    def delete(self, id_: int) -> None:
        self.cursor.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            "WHERE id = %s",
            (id_,)
        )
        self._connection.commit()

