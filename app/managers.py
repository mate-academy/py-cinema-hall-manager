import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cinema")
        self.cursor = self.conn.cursor()
        self.table_name = "actors"

    def create_table(self) -> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT)
        """)
        self.conn.commit()

    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")

        return [Actor(*row) for row in self.cursor.fetchall()]

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(f"INSERT INTO {self.table_name} "
                            "VALUES (first_name = ?, last_name = ?)",
                            (first_name, last_name))

        self.conn.commit()

    def update(self,
               new_id: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self.cursor.execute(f"UPDATE {self.table_name} "
                            "SET first_name = ?, last_name = ? "
                            "WHERE id = ?",
                            (new_id, new_first_name, new_last_name))
        self.conn.commit()

    def delete(self, id_to_delete: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?",
                            (id_to_delete,))
        self.conn.commit()


if __name__ == "__main__":
    Actor.objects = ActorManager()
    Actor.objects.create_table()
    print(Actor.objects.all())
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
