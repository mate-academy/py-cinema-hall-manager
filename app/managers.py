# import sqlite3
#
# # from models import Actor
#
#
# class ActorManager:
#     def __init__(self) -> None:
#         self._connection = sqlite3.connect("cinema.sqlite")
#         self.table_name = "actors"
#
# # create
#     def create(self, first_name: str, last_name: str) -> None:
#         self._connection.execute(
#             f"INSERT INTO {self.table_name}"
#             f" (first_name, last_name) VALUES (?, ?)",
#             (first_name, last_name)
#         )
#         self._connection.commit()
#
# # retrieve
#     def all(self) -> list:
#         actors_cursor = self._connection.execute(
#             "SELECT * FROM actors"
#         )
#         for row in actors_cursor:
#             print(row)
#         # actors_cursor = self._connection.execute(
#         #     f"SELECT * FROM {self.table_name}"
#         # )
#         # return [
#         #     Actor(*row) for row in actors_cursor
#         # ]
#
# # update
#     def update(
#             self,
#             id_to_update: int,
#             first_name: str,
#             last_name: str
#     ) -> None:
#         self._connection.execute(
#             f"UPDATE {self.table_name} "
#             f"SET first_name = ?, last_name = ? WHERE id = ?",
#             (first_name, last_name, id_to_update)
#         )
#         self._connection.commit()
#
# # delete
#     def delete(self, id_to_delete: int) -> None:
#         self._connection.execute(
#             f"DELETE FROM {self.table_name} WHERE id = ?",
#             (id_to_delete)
#         )
#         self._connection.commit()
import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.db")
        self.table_name = "actors"

    def create(
            self,
            first_name: str,
            last_name: str
    ) -> int:
        cursor = self.connection.execute(
            """INSERT INTO actors (first_name, last_name)
            VALUES (?, ?)""",
            (first_name, last_name),
        )
        return cursor.lastrowid

    def all(self) -> list[Actor]:
        cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str) -> None:
        self.connection.execute(
            """UPDATE actors
            SET first_name = ?, last_name = ?
            WHERE id = ?""",
            (first_name, last_name, actor_id),
        )

    def delete(self, actor_id: int) -> None:
        self.connection.execute(
            """DELETE FROM actors
            WHERE id = ?""",
            (actor_id,)
        )