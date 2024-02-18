import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connector = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    # CREATE 'CRUD' FUNCTIONS
    def create(self, first_name: str, last_name: str) -> None:
        self._connector.execute(
            f"INSERT INTO {self.table_name } VALUES (first_name, last_name); "
        )
