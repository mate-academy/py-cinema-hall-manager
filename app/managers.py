import sqlite3

from models import Actor

class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema")
        self.table_name = "actors"

    def all(self):
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in actor_cursor
        ]

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id, first_name, last_name):
        self._connection.execute(
            f"Update {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, id)
        )
        self._connection.commit()

    def delete(self, id):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
     (id,)
        )
        self._connection.commit()


# if __name__ == "__main__":
#     manager = ActorManager()
    # manager.create("Artur", "Bashyrov")
    # manager.update("2", "Bashyrov", "Artur")
    # manager.delete("1")
    # print(manager.all())