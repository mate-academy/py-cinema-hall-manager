import psycopg2
from psycopg2 import Error

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        try:
            self._connection = psycopg2.connect(
                host="localhost",
                database="cinema",
                user="postgres",
                password="15vktelefon",
                port=5432,
            )

            self._table_name = "actors"

            print("Successful connect")
        except (Exception, Error) as err:
            print("Error", err)

    def all(self) -> list[Actor]:
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM actors")

        return [
            Actor(*row)
            for row in cursor.fetchall()
        ]

    def create(self, first_name: str, last_name: str) -> None:
        cursor = self._connection.cursor()

        cursor.execute(
            f"INSERT INTO {self._table_name} (first_name, last_name) VALUES (%s, %s)",
            (first_name, last_name))

        self._connection.commit()

    def update(
            self,
            actor_id: int,
            first_name: str,
            last_name: str
    ) -> None:
        cursor = self._connection.cursor()

        cursor.execute(f"UPDATE {self._table_name} "
                       "SET first_name = %s, "
                       "last_name = %s "
                       "WHERE id = %s ",
                       (first_name, last_name, actor_id)
                       )

        self._connection.commit()

    def delete(self, actor_id) -> None:
        cursor = self._connection.cursor()

        cursor.execute(f"DELETE FROM {self._table_name} WHERE id = %s", (actor_id,))

        self._connection.commit()

