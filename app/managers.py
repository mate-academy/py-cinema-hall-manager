import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema_db.sqlite")
