from models import Actor
import psycopg2


class ActorManager:
    def __init__(self) -> None:
        self._db_name = "cinema"
        self._password = "mate"
        self._username = "mate"
        self.last_id = 0

    def _connect(self) -> None:
        return psycopg2.connect(user=self._username,
                                password=self._password,
                                host="127.0.0.1",
                                port="5432",
                                database=self._db_name)

    def create(self, first_name: str, last_name: str) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()

            query = """
                    INSERT INTO actor(id, first_name, last_name)
                    VALUES (%s,%s,%s);
                    """
            self.last_id += 1
            cursor.execute(query, (self.last_id, first_name, last_name))

    def all(self) -> list[Actor]:
        with self._connect() as conn:
            cursor = conn.cursor()

            query = """
                    SELECT * FROM actor;
                    """

            cursor.execute(query)
            actors_data = cursor.fetchall()
            actors = [Actor(row[0], row[1], row[2]) for row in actors_data]
            return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()

            query = """
                    UPDATE actor SET first_name = %s, last_name = %s
                    WHERE id = %s;
                    """
            cursor.execute(query, (first_name, last_name, id))

    def delete(self, id: int) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()

            query = """
                    DELETE FROM actor
                    WHERE id = %s;
                    """

            self.last_id += 1
            cursor.execute(query, (id,))
