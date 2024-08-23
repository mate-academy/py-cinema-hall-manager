from dataclasses import dataclass


@dataclass
class Actor:
    id: int | None
    first_name: str
    last_name: str


# Create a database cinema where will be stored
# entries with data about different actors and actresses.
# Create a table actors with corresponding columns.
#
# import sqlite3
#
#
# def create_database() -> None:
#     _connection = sqlite3.connect("cinema.db")
#
#     _connection.cursor().execute('''
#     CREATE TABLE IF NOT EXISTS actors (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL
#     )
#     ''')
#
#     _connection.commit()
#     _connection.close()
#
# create_database()
