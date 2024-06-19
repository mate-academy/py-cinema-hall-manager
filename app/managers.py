import sqlite3
from models import Actor
from typing import Any


class ActorManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("identifier.sqlite")
        self.cursor = self.conn.cursor()

    def create(self, first_name: str, last_name: str) -> Any:
        query = ("INSERT INTO actor_manager (first_name, last_name)"
                 " VALUES (?, ?)")
        self.cursor.execute(query, (first_name, last_name))
        self.conn.commit()
        return self.cursor.lastrowid

    def all(self) -> Any:
        query = ("SELECT id, first_name, last_name "
                 "FROM actor_manager")
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [
            Actor(id=row[0],
                  first_name=row[1],
                  last_name=row[2]) for row in results
        ]

    def update(
            self,
            actor_id: int,
            first_name: str,
            last_name: str
    ) -> Any:
        query = ("UPDATE actor_manager "
                 "SET first_name = ?, last_name = ? "
                 "WHERE id = ?")
        self.cursor.execute(
            query,
            (first_name, last_name, actor_id)
        )
        self.conn.commit()

    def delete(self, actor_id: int) -> Any:
        query = "DELETE FROM actor_manager WHERE id = ?"
        self.cursor.execute(query, (actor_id,))
        self.conn.commit()
