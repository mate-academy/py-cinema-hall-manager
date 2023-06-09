from dataclasses import is_dataclass
from datetime import datetime
from typing import Any
from functools import wraps


class EntityHelper:
    __placeholder_symbol = "?"

    def __init__(self, entity_type: type, table_name: str) -> None:
        if not is_dataclass(entity_type):
            raise ValueError(f"EntityHelper is able to work with "
                             f"dataclasses only. {type} is not a dataclass")
        self.__entity_type: type = entity_type
        self.__table_name: str = table_name
        self.__entity_type_fields: tuple = tuple(
            self.__entity_type
            .__dataclass_fields__
            .keys()
        )
        self.__insert_into_statement: str = (
            f"insert into '{self.__table_name}' "
            f"{self.__entity_type_fields[1:]} values "
            f"({self.make_placeholders(len(self.__entity_type_fields) - 1)})"
        )
        self.__select_all_statement: str = (
            f"select * from {self.__table_name}"
        )
        self.__delete_statement: str = (
            f"delete from {self.__table_name} where "
            f"id={self.__placeholder_symbol}"
        )
        self.get_entity_values = (
            self
            .validate_entity_type(self.__entity_type)
            (self.get_entity_values)
        )
        self.get_update_statement = (
            self
            .validate_entity_type(self.__entity_type)
            (self.get_update_statement)
        )

    @classmethod
    def make_placeholders(cls, count: int = 1) -> str:
        return ",".join([cls.__placeholder_symbol for _ in range(count)])

    def get_entity_values(self, obj: Any) -> tuple:
        return tuple(obj.__dict__.values())

    def get_update_statement(self, obj: Any) -> str:
        parameters = tuple(
            f"{key}='{value}'"
            if isinstance(value, (str, datetime))
            else f"{key}={value}"
            for key, value in obj.__dict__.items()
        )
        return (
            f"update {self.__table_name} "
            f"set {', '.join(parameters[1:])} "
            f"where {parameters[0]}"
        )

    def get_select_all_statement_param(self) -> str:
        return self.__select_all_statement

    def get_insert_statement_param(self) -> str:
        return self.__insert_into_statement

    def get_delete_statement_param(self) -> str:
        return self.__delete_statement

    def validate_entity_type(self, entity_type: type) -> callable:
        def decorator(func: callable) -> callable:
            @wraps(func)
            def wrapper(obj: Any) -> Any:
                if not isinstance(obj, entity_type):
                    raise TypeError(
                        f"Object must be of type {entity_type.__name__}"
                        f", not {type(obj).__name__}"
                    )
                return func(obj)
            return wrapper
        return decorator
