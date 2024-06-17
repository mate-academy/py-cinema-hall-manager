import sqlite3


def create_database() -> None:
    conn = sqlite3.connect('cinema.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
