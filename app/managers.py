import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        self.conn = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self):
        actors = self.conn.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actors]

    def create(self, first_name, last_name):
        self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name))
        self.conn.commit()

    def update(self, id, name, surname):
        self.conn.execute(f"UPDATE {self.table_name} "
                          "SET first_name = ?, last_name= ?"
                          "WHERE id = ?",
                          (name, surname, id))
        self.conn.commit()

    def delete(self, id):
        self.conn.execute(f"DELETE FROM {self.table_name} "
                          f"WHERE id = ?",
                          (id,))
        self.conn.commit()
if __name__ == '__main__':
    manager = ActorManager()
    print(manager.all())
    manager.delete(4)
    print(manager.all())
