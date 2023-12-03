import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_path='cinema.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
        )
        '''
        self.conn.execute(query)

    def create(self, first_name, last_name):
        query = 'INSERT INTO actors (first_name, last_name) VALUES (?, ?)'
        self.conn.execute(query, (first_name, last_name))
        self.conn.commit()

    def all(self):
        query = 'SELECT * FROM actors'
        cursor = self.conn.execute(query)
        actors = [Actor(*row) for row in cursor.fetchall()]
        return actors

    def update(self, actor_id, first_name=None, last_name=None):
        actor = self.get_actor_by_id(actor_id)

        if actor:
            if first_name:
                actor.first_name = first_name
            if last_name:
                actor.last_name = last_name

            query = 'UPDATE actors SET first_name=?, last_name=? WHERE id=?'
            self.conn.execute(query, (actor.first_name, actor.last_name, actor.id))
            self.conn.commit()

    def delete(self, actor_id):
        query = 'DELETE FROM actors WHERE id=?'
        self.conn.execute(query, (actor_id,))
        self.conn.commit()

    def get_actor_by_id(self, actor_id):
        query = 'SELECT * FROM actors WHERE id=?'
        cursor = self.conn.execute(query, (actor_id,))
        actor_data = cursor.fetchone()

        if actor_data:
            return Actor(*actor_data)
        else:
            return None