import sqlite3

from models import Actor


class ActorManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect("./cinema.sqlite")
        self.cursor = self._connection.cursor()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?, ?);",
            (first_name, last_name)
        )
        self._connection.commit()
        return self.cursor.lastrowid

    def all(self) -> list:
        cursor = self._connection.execute(
            "SELECT * FROM actors;"
        )
        # return list of actors
        return [
            Actor(*row) for row in cursor.fetchall()
        ]

    def update(
            self, id: int, first_name: str = None, last_name: str = None
    ) -> None:
        updates = []
        values = []
        if first_name:
            updates.append("first_name = ?")
            values.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            values.append(last_name)
        values.append(id)

        query = f"UPDATE actors SET {', '.join(updates)} WHERE id = ?;"
        self.cursor.execute(query, values)
        self._connection.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM actors WHERE id=?;", (id,))
        self._connection.commit()


if __name__ == "__main__":
    pass
