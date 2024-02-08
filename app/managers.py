import sqlite3
from models import Actor


class ActorManager:
    def __init__(self, table_actors: str) -> None:
        self.conn = sqlite3.connect("C:/projects/py-actor-manager/identifier.sqlite")
        self.cursor = self.conn.cursor()
        self.table_actors = table_actors

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"""
            INSERT INTO {self.table_actors} 
            (first_name, last_name) 
            VALUES (?, ?)
            """,
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_actors}")
        rows = self.cursor.fetchall()
        return [Actor(*row) for row in rows]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f"""
            UPDATE {self.table_actors}
            SET 
                first_name = ?, 
                last_name = ? 
            WHERE 
                id = ?
            """,
            (first_name, last_name, actor_id)
        )
        self.conn.commit()

    def delete(self, actor_id: int) -> None:
        self.cursor.execute(
            f"""
            DELETE FROM {self.table_actors} 
            WHERE id = ?
            """,
            (actor_id,)
        )
        self.conn.commit()
