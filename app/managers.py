import sqlite3
from models import Actor


class CinemaManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            "INSERT INTO Actors (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        cinema_cursor = self._connection.execute(
            "SELECT * FROM Actors"
        )
        actors = [Actor(*row) for row in cinema_cursor]
        cinema_cursor.close()
        return actors

    def update(self, _id: int, new_name: str, new_last_name: str) -> None:
        self._connection.execute(
            "UPDATE Actors SET first_name = ?, last_name = ? WHERE id = ?",
            (new_name, new_last_name, _id)
        )
        self._connection.commit()

    def delete(self, _id: int) -> None:
        self._connection.execute(
            "DELETE FROM Actors WHERE id = ?",
            (_id,)
        )

    def disconnect(self) -> None:
        self._connection.close()


if __name__ == "__main__":
    manager = CinemaManager()
    manager.create("Taras", "Bulba")
    print(manager.all())
    manager.update(1, "Petya", "Poroh")
    print(manager.all())
    manager.delete(1)
    manager.disconnect()
