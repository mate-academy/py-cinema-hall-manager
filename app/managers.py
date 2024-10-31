import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = 'actors'
        self.connection = sqlite3.connect('cinema.sqlite')


    def create(self, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()


    def all(self) -> list:
        cinema_cursor = self.connection.execute(
            f'SELECT * FROM {self.table_name}'
        )
        return [
            Actor(*row) for row in cinema_cursor
        ]

    def update(self, id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?",
            (first_name, last_name, id)
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id,)
        )


if __name__ == '__main__':
    manager = ActorManager()
    manager.all()