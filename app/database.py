import sqlite3


def create_database() -> None:
    conn = sqlite3.connect("cinema.db")
    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
    """
    )
    conn.commit()
    conn.close()


create_database()
