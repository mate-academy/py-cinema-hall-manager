import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect(
            "/MateProjectsPython/py-actor-manager/cinema.sqlite"
        )

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actor_manager_cursor = self._connection.execute(
            "SELECT * FROM actors"
        )
        # print(f"actor_manager_cursor: {actor_manager_cursor}")
        # for row in actor_manager_cursor:
        #     print(row)
        return [
            Actor(*row) for row in actor_manager_cursor
        ]

    def update(
            self,
            id_to_update: int,
            new_actor_first_name: str,
            new_actor_last_name: str
    ) -> None:
        self._connection.execute(
            "UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (
                new_actor_first_name,
                new_actor_last_name,
                id_to_update
            )
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ? ",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == "__main__":
    manager = ActorManager()
    manager.create("Brad", "Pitt")
    print(manager.all())
