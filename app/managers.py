import sqlite3

from models import Actor


class ActorManager:
    "Create ActorManager class"

    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"
