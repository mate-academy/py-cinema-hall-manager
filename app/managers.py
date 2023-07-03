import sqlite3


from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self._table_name = "actors"

    def all(self) -> list:
        sql = (f"SELECT id, first_name, last_name "
               f"FROM {self._table_name}")
        cursor = self._connection.execute(sql)
        return [Actor(*data) for data in cursor]

    def create(self, first_name: str, last_name: str) -> None:
        sql = (f"INSERT INTO {self._table_name} "
               "(first_name, last_name) VALUES (?, ?)")
        self._connection.execute(sql, (first_name, last_name))
        self._connection.commit()

    def update(self, id: int,
               first_name: str,
               last_name: str) -> None:
        sql = (f"UPDATE {self._table_name} "
               f"SET first_name = ?, last_name = ? "
               f"WHERE id = {id}")
        self._connection.execute(sql, (first_name, last_name))
        self._connection.commit()

    def delete(self, id_to_del: int) -> None:
        sql = (f"DELETE FROM {self._table_name} "
               f"WHERE id = ?")
        self._connection.execute(sql, (id_to_del, ))
        self._connection.commit()
