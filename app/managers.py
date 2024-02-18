import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connector = sqlite3.connect("..//cinema.sqlite")
        self.table_name = "actors"

    # CREATE 'CRUD' FUNCTIONS
    def create(self, first_name: str, last_name: str) -> None:
        self._connector.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES ('{first_name}', '{last_name}'); "
        )
        self._connector.commit()

    def all(self) -> list[Actor]:
        persons = self._connector.execute("SELECT * FROM actors; ")
        return [Actor(*person) for person in persons]

    def update(self, index: int, f_name: str, l_name: str) -> None:
        self._connector.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = '{f_name}', "
            f"last_name = '{l_name}' "
            f"WHERE id = {index}; "
        )
        self._connector.commit()

    def delete(self, index: int) -> None:
        self._connector.execute(
            f"DELETE FROM {self.table_name} WHERE id = {index}; ")
