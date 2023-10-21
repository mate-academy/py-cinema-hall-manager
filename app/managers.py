import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect(
            "C:/Users/andsh/PycharmProjects/MyProjects"
            "/django_orm/tasks_with_git_fork_2/py-actor-manager"
            "/cinema.db3"
        )
        self.tablename = "actors"

    def all(self):
        actors_data = self._connection.execute(
            f"SELECT * FROM {self.tablename}"
        )
        print("Actors data", actors_data)
        return [Actor(*row) for row in actors_data]

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.tablename} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.tablename} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.tablename} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == '__main__':
    actor = ActorManager()
    print(actor.all())
    print()
    actor.create("bodya", "messi")
    print(actor.all())
    print()
    actor.update(3, "ya",  "actor")
    print(actor.all())
    print()
    actor.delete(4)
    print(actor.all())
