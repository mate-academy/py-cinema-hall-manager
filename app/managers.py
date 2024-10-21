import os
import sqlite3


class ActorManager :
    def __init__(self):
        # Отримання поточної робочої директорії
        current_directory = os.getcwd()

        # Виведення поточної директорії
        print("Поточна робоча директорія:", current_directory)

        self._connection = sqlite3.connect("./../cinema.sqlite")
        self.table_name = "cinema_actors"

    # CREATE - C
    def create(self, **kwargs):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (kwargs['first_name'], kwargs['last_name'],)
        )
        self._connection.commit()

    # RETRIEVE - R
    def all(self):
        format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name} "
        )
        rows = []
        print("format  id")
        for row in format_cursor:
            print(row)
            rows.append(row)
        return rows


    # UPDATE - U
    def update(self, id_to_update: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ? ",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    # DELETE - D
    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE "
            f"FROM {self.table_name} "
            f"WHERE id = ? ",
            (id_to_delete,)
        )
