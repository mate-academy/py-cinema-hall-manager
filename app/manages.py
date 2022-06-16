import sqlite3
from models import Actor

class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect('cinema.sqlite')
        self.table_name = 'actor'


    def create(self, first_name_, last_name_):
        self._connection.execute(f"INSERT INTO {self.table_name} (first_name, last_name) "
                                 f"VALUES (?,?)",
                                 (first_name_, last_name_))
        self._connection.commit()

    def all(self):
        cinema_data = self._connection.execute(f"SELECT * FROM {self.table_name}")
        print('cinema_data', cinema_data)
        return [Actor(*row) for row in cinema_data]

    def update(self, first_name_:str, last_name_:str, id_to_update:int, ):
        self._connection.execute(
            f"UPDATE {self.table_name}"
            " SET first_name = ?, last_name=?"
            " WHERE id=?", (last_name_, first_name_, id_to_update))

        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(f"DELETE FROM {self.table_name}"
                                 f" WHERE id = ?", (id_to_delete,))
        self._connection.commit()


if __name__ == '__main__':
    manager = ActorManager()
    manager.delete(2)
