import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.connect = sqlite3.connect("../cinema.sqlite")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        sql = f"INSERT INTO {self.table_name} " \
              "(first_name,last_name) VALUES (?,?)"
        self.connect.execute(sql, (first_name, last_name))
        self.connect.commit()

    def all(self) -> None:
        actors = self.connect.execute(f"SELECT * "
                                      f"FROM {self.table_name}")
        return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        sql = f"UPDATE {self.table_name} " \
              "SET first_name = ?, last_name = ? " \
              "WHERE id = ?"
        self.connect.execute(sql, (first_name, last_name, id))
        self.connect.commit()

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {self.table_name} " \
              "WHERE id = ?"
        self.connect.execute(sql, (id,))
        self.connect.commit()
