import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) ->None:
        self._connection = sqlite3.connect("cinema")

    def all(self) -> None:
        actor_data = self._connection.execute("SELECT * FROM actors")
        print(actor_data)


if __name__ == '__main__':
    manager = ActorManager()
    manager.all()
