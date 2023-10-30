from models import Actor
import psycopg2


class ActorManager:
    def __init__(self) -> None:
        self.last_id = 0
        self.connection = None

    def _connect(self) -> None:
        self.connection = psycopg2.connect(user="mate",
                                           password="mate",
                                           host="127.0.0.1",
                                           port="5432",
                                           database="cinema")

    def create(self, first_name: str, last_name: str) -> None:
        try:
            self._connect()
            cursor = self.connection.cursor()

            query = """
                    INSERT INTO actor(id, first_name, last_name)
                    VALUES (%s,%s,%s);
                    """
            self.last_id += 1
            cursor.execute(query, (self.last_id, first_name, last_name))
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def all(self) -> list[Actor]:
        try:
            self._connect()
            cursor = self.connection.cursor()

            query = """
                    SELECT * FROM actor;
                    """

            cursor.execute(query)
            actors_data = cursor.fetchall()
            actors = [Actor(row[0], row[1], row[2]) for row in actors_data]
            return actors
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def update(self, id: int, first_name: str, last_name: str) -> None:
        try:
            self._connect()
            cursor = self.connection.cursor()

            query = """
                    UPDATE actor SET first_name = %s, last_name = %s
                    WHERE id = %s;
                    """
            cursor.execute(query, (first_name, last_name, id))
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def delete(self, id: int) -> None:
        try:
            self._connect()
            cursor = self.connection.cursor()

            query = """
                    DELETE FROM actor
                    WHERE id = %s;
                    """
            self.last_id += 1
            cursor.execute(query, (id,))
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
