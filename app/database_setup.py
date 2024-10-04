import sqlite3


def setup_database() -> None:
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    setup_database()
    print("Database and actors table created.")
