import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            'SELECT * FROM actors'
        )
        return print([Actor(*row) for row in cursor.fetchall()])
    
    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()
        return print(f"Actor {first_name} {last_name} created")
    
    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id = ?",
            (first_name, last_name, actor_id)
        )
        self._connection.commit()
        return print(f"Actor {actor_id} updated")
    
    def delete(self, actor_id: int) -> None:
        self._connection.execute(
            "DELETE FROM actors WHERE id = ?",
            (actor_id,)
        )
        self._connection.commit()
        return print(f"Actor {actor_id} deleted")

if __name__ == "__main__":
    manager = ActorManager()
