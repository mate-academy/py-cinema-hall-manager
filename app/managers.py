import sqlite3

from models import Actor

class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect('C:/Users/taras/projects/py-actor-manager/cinema.sqlite')
        self.table_name = 'actors'

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO 'actors' (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self._connection.commit()

    def all(self):
        actor_manager_cursor = self._connection.execute(
            "SELECT * FROM 'actors'"
        )

        return [
            Actor(*row) for row in actor_manager_cursor
            ]

    def update(self, id_to_update: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATE 'actors' "
            f"SET first_name=?, last_name=? "
            f"WHERE id=?",
            (first_name, last_name, id_to_update)
        )

        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM 'actors' "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()
# if __name__ == "__main__":
#     Actor.objects = ActorManager()
#     # Actor.objects.create(first_name="Emma", last_name="Watson")
#     Actor.objects.all()