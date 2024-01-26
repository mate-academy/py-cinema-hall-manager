import sqlite3


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("actors")
