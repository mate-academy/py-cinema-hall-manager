import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cin")