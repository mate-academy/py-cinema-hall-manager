from sqlite3 import Connection, connect
from entity_helper import EntityHelper
from models import Actor
from os import path


class ActorManager:
    def __init__(self) -> None:
        db_path = path.join(path.dirname(path.abspath(__file__)), "cinema.db3")
        self.__connector: Connection = connect(db_path)
        self.__actor_helper: EntityHelper = EntityHelper(Actor, "actors")

    def __del__(self) -> None:
        if self.__connector:
            self.__connector.close()

    def create(self, actor: Actor) -> None:
        cursor = self.__connector.execute(
            self.__actor_helper.get_insert_statement_param(),
            self.__actor_helper.get_entity_values(actor)[1:]
        )
        self.__connector.commit()
        actor.id = cursor.lastrowid

    def all(self) -> list[Actor]:
        cursor = self.__connector.execute(
            self.__actor_helper.get_select_all_statement_param()
        )
        return [
            Actor(*actor_info) for actor_info in cursor.fetchall()
        ]

    def update(self, actor: Actor) -> None:
        self.__connector.execute(
            self
            .__actor_helper
            .get_update_statement(actor)
        )
        self.__connector.commit()

    def delete(self, id: int) -> None:
        self.__connector.execute(
            self.__actor_helper.get_delete_statement_param(),
            str(id)
        )
        self.__connector.commit()
